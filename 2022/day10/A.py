import sys

with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: l.split(),f.readlines()))

i = 1

ans = 0
x = 1
for line in lines:
    if i % 40 == 20:
        ans += i * x
    if line[0] == "noop":
        i += 1
        continue
    if i % 40 == 19:
        ans += (i+1)*x
    x += int(line[1])
    i += 2

print(ans)
