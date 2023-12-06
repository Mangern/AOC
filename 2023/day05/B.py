import sys
from collections import deque

def erase_range(r, a, b):
    nr = []
    for i in range(len(r)):
        x, y = r[i]
        ia = max(a, x)
        ib = min(b, y)

        if ia > ib:
            nr.append([x, y])
            continue

        if ia > x:
            nr.append([x, ia-1])
        if ib < y:
            nr.append([ib+1, y])
    return nr

def transfer(src, dst):
    # Add everything from src not in dst to dst
    for x, y in dst:
        src = erase_range(src, x, y)

    for x, y in src:
        dst.append([x, y])



lines = open(sys.argv[1]).readlines()

seeds = list(map(int, lines[0].split(": ")[-1].split()))


rs = [[]]
for a, b in zip(seeds[::2], seeds[1::2]):
    rs[-1].append([a, a + b - 1])

cmp = None

for line in lines[1:]:
    if line == "\n":
        cmp = None
    elif cmp is None:
        s, t = line.split()[0].split("-to-")
        cmp = (s, t)

        if len(rs) >= 2:
            transfer(rs[-2], rs[-1])

        rs.append([])
    else:
        t_range, s_range, sz = list(map(int, line.split()))
        delta = t_range - s_range

        sa, sb = s_range, s_range + sz - 1

        for a, b in rs[-2]:
            ia = max(a, sa)
            ib = min(b, sb)
            if ia > ib:
                continue
            #rs[-1] = erase_range(rs[-1], ia+delta, ib+delta)
            rs[-1].append([ia+delta,ib+delta])

transfer(rs[-2], rs[-1])
for r in rs:
    print(sorted(r))

print()
print(sorted(rs[-1])[0])
print(sorted(rs[-1])[1])
