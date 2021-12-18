def p1():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    def evaluate(line):
        stack = []
        match = {
            ")": "(",
            "]": "[",
            "}": "{",
            ">": "<"
        }
        points = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }
        for c in line:
            if c in match:
                if len(stack) == 0 or stack[-1] != match[c]:
                    return points[c]
                else:
                    stack.pop()
            else:
                stack.append(c)
        return 0


    ans = sum([evaluate(line) for line in lines])
    print(ans)

def p2():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    def evaluate(line):
        stack = []
        match = {
            ")": "(",
            "]": "[",
            "}": "{",
            ">": "<",
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }
        points = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4 
        }
        for c in line:
            if c in points:
                if len(stack) == 0 or stack[-1] != match[c]:
                    return -1 
                else:
                    stack.pop()
            else:
                stack.append(c)
        ps = [points[match[c]] for c in reversed(stack)]

        score = 0

        for p in ps:
            score = 5 * score + p
        return score


    scores = [evaluate(line) for line in lines if evaluate(line) != -1]
    scores.sort()

    ans = scores[len(scores)>>1]
    print(ans)

p2()
