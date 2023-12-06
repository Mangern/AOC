import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

t = int("".join(lines[0].split()[1:]))
d = int("".join(lines[1].split()[1:]))

ans = 0

for i in range(t+1):
    if i * (t - i) > d:
        ans += 1
print(ans)
