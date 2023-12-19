"""
Super Duper Object Oriented solution!!!
Writing classes is so much fun.
Hopefully, making this object oriented and everything
will make part two super easy
"""
import sys

class Part:
    def __init__(self, part_str):
        assert part_str[0] == '{'
        assert part_str[-1] == '}'

        vars = part_str[1:-1].split(",")
        vals = [int(var.split("=")[-1]) for var in vars]

        self.x = vals[0]
        self.m = vals[1]
        self.a = vals[2]
        self.s = vals[3]
        self.part_sum = sum(vals)

class RuleCheck:
    def __init__(self, check_str):
        self.field = check_str[0]
        self.op = check_str[1]

        sep_idx = check_str.find(":")

        self.threshold = int(check_str[2:sep_idx])
        self.next_id = check_str[sep_idx + 1:]

    def evaluate_part(self, part: Part):
        cur_val = part.__dict__[self.field]

        if self.op == '>' and cur_val > self.threshold:
            return self.next_id

        if self.op == '<' and cur_val < self.threshold:
            return self.next_id

        return None


class Rule:
    def __init__(self, rule_str):
        check_strs = rule_str.split(",")
        self.checks = [RuleCheck(s) for s in check_strs[:-1]]
        self.fallback = check_strs[-1]

    def get_next(self, part: Part):
        for check in self.checks:
            res = check.evaluate_part(part)
            if res:
                return res
        return self.fallback

class Machine:
    def __init__(self):
        self.rules = dict()

    def add_rule(self, rule_str):
        start_body = rule_str.find('{')
        assert start_body != -1, "Invalid rule"
        assert rule_str[-1] == '}', "Invalid rule"

        rule_id = rule_str[:start_body]
        rule_body = rule_str[start_body + 1:-1]

        self.rules[rule_id] = Rule(rule_body)

    def evaluate(self, part: Part):
        rule_id = "in"
        while True:
            assert rule_id in self.rules, f"Unknown rule encountered {rule_id}"
            next_rule_id = self.rules[rule_id].get_next(part)
            if next_rule_id == "A":
                return True
            elif next_rule_id == "R":
                return False
            rule_id = next_rule_id

machine_lines, part_lines = (
    map(
        lambda s: s.splitlines(),
        open(sys.argv[1]).read().split("\n\n")
    ))

machine = Machine()
for line in machine_lines:
    machine.add_rule(line)

ans = 0
for line in part_lines:
    part = Part(line)

    if machine.evaluate(part):
        ans += part.part_sum

print(ans)
