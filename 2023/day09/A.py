import sys

def extr(a):
    rows = [a]

    while True:
        b = [y - x for x, y in zip(rows[-1], rows[-1][1:])]
        rows.append(b)
        if not any(b):
            break


    n = len(rows)

    for i in range(n - 2, -1, -1):
        rows[i].append(rows[i][-1] + rows[i+1][-1])
    return rows[i][-1]


with open(sys.argv[1]) as f:
    lines = f.readlines()

ans = 0
for line in lines:
    a = list(map(int, line.split()))

    ans += extr(a)

print(ans)
