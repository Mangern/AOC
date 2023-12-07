import sys

def intersect(a, b, c, d):
    if a > d or b < c:
        return None, None
    return (max(a,c), min(b,d))


def traverse(l, r, rs, i = 0):
    if i == len(rs):
        return set([(l, r)])

    did_match = False
    result = set()
    for (sl, sr), (tl, tr) in rs[i]:
        ia, ib = intersect(l, r, sl, sr)
        if ia is None:
            continue

        did_match = True
        result |= traverse(ia + tl - sl, ib + tl - sl, rs, i+1)

        if ia > l:
            result |= traverse(l, ia-1, rs, i)
        if ib < r:
            result |= traverse(ib+1, r, rs, i)

    if not did_match:
        result |= traverse(l, r, rs, i+1)
    return result

lines = open(sys.argv[1]).readlines()
initial = list(map(int, lines[0].split(": ")[-1].split()))

seeds = []
for a, b in zip(initial[::2], initial[1::2]):
    seeds.append((a, a + b - 1))

cmp = None
rs = []

for line in lines[1:]:
    if line == "\n":
        cmp = None
    elif cmp is None:
        s, t = line.split()[0].split("-to-")
        cmp = s
        rs.append([])
    else:
        t_range, s_range, sz = list(map(int, line.split()))

        rs[-1].append((
            (s_range, s_range + sz - 1),
            (t_range, t_range + sz - 1)
        ))

result = set()
for l, r in seeds:
    result |= traverse(l, r, rs, 0)

print(min(result)[0])
