import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

t = list(map(int, lines[0].split()[1:]))
d = list(map(int, lines[1].split()[1:]))

ans = 1
for i in range(len(t)):
    res = 0
    for j in range(1, t[i]+1):
        if (t[i] - j) * j > d[i]:
            res += 1
    ans *= res

print(ans)
