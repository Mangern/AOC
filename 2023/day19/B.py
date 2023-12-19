"""
Super Duper Object Oriented solution!!!
Doing part 2 was easy: Just remove some classes!
"""
import sys

class RuleCheck:
    def __init__(self, check_str):
        self.field = check_str[0]
        self.op = check_str[1]

        sep_idx = check_str.find(":")

        self.threshold = int(check_str[2:sep_idx])
        self.next_id = check_str[sep_idx + 1:]

    def get_accept_range(self):
        if self.op == '>':
            return (self.threshold + 1, 4000)
        else:
            return (1, self.threshold - 1)


class Rule:
    def __init__(self, rule_str):
        check_strs = rule_str.split(",")
        self.checks = [RuleCheck(s) for s in check_strs[:-1]]
        self.fallback = check_strs[-1]


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

    def intersect_range(self, ran_A, ran_B):
        return (max(ran_A[0], ran_B[0]), min(ran_A[1], ran_B[1]))

    def intersect(self, ran_obj_A, ran_obj_B):
        return {
            "x": self.intersect_range(ran_obj_A["x"], ran_obj_B["x"]),
            "m": self.intersect_range(ran_obj_A["m"], ran_obj_B["m"]),
            "a": self.intersect_range(ran_obj_A["a"], ran_obj_B["a"]),
            "s": self.intersect_range(ran_obj_A["s"], ran_obj_B["s"]),
        }
    
    def erase_range(self, ran_obj, field, exclude_ran):
        result = []
        cur = ran_obj[field]

        exclude_ran = self.intersect_range(cur, exclude_ran)

        if exclude_ran[0] > cur[0]:
            nxt = {k: v for k, v in ran_obj.items()}
            nxt[field] = (cur[0], exclude_ran[0] - 1)
            result.append(nxt)

        if exclude_ran[1] < cur[1]:
            nxt = {k: v for k, v in ran_obj.items()}
            nxt[field] = (exclude_ran[1] + 1, cur[1])
            result.append(nxt)

        return result

    def is_empty(self, ran_obj):
        for _, ran in ran_obj.items():
            if ran[1] < ran[0]:
                return True

        return False

    def get_accepted_ranges(self, rule_id = "in"):
        if rule_id == "A":
            return [{"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)}]
        if rule_id == "R":
            return []

        result = []
        curr_rule = self.rules[rule_id]

        curr_accept_ran = [{"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)}]

        for rule_check in curr_rule.checks:
            check_field = rule_check.field
            check_ran = rule_check.get_accept_range()

            sub_ranges = self.get_accepted_ranges(rule_check.next_id)

            for accept_obj in curr_accept_ran:
                for obj in sub_ranges:
                    res = self.intersect(obj, accept_obj)
                    res[check_field] = self.intersect_range(res[check_field], check_ran)
                    result.append(res)

            next_accept = []

            for accept_obj in curr_accept_ran:
                for result_obj in self.erase_range(accept_obj, check_field, check_ran):
                    if not self.is_empty(result_obj):
                        next_accept.append(result_obj)
            curr_accept_ran = next_accept

        last_ranges = self.get_accepted_ranges(curr_rule.fallback)
        for accept_obj in curr_accept_ran:
            for obj in last_ranges:
                result.append(self.intersect(obj, accept_obj))

        return [res_obj for res_obj in result if not self.is_empty(res_obj)]

machine_lines, _ = (
    map(
        lambda s: s.splitlines(),
        open(sys.argv[1]).read().split("\n\n")
    ))

machine = Machine()
for line in machine_lines:
    machine.add_rule(line)

ans = 0
for ran_thing in machine.get_accepted_ranges():
    res = 1
    for _, ran in ran_thing.items():
        res *= (ran[1] - ran[0] + 1)
    ans += res

print(ans)
