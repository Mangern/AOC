from functools import reduce
with open("input", "r") as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))


ans = sorted(reduce(lambda curr, x: curr + [0] if x == "" else curr[:-1] + [curr[-1] + int(x)], lines, [0]))

print(sum(ans[-3:]))

