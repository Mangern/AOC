from itertools import combinations
from sys import stdin

adj = {}

for line in stdin:
    line = line.strip()
    if not line:
        break
    a,b = map(int, line.split('|'))
    adj[a] = adj.get(a, []) + [b]

ans = 0
inv = []
for line in stdin:
    nums = list(map(int, line.strip().split(',')))

    valid = True
    for a,b in combinations(nums, 2):
        if (b in adj) and (a in adj[b]):
            valid = False
            break
    if valid:
        ans += nums[len(nums)//2]
    else:
        inv.append(nums)
print(f"Part 1: {ans}")


ans = 0
for nums in inv:
    s = set(nums)

    res = []

    while s:
        add = -1
        cnt_add = float('inf')
        for x in s:
            cnt_in = 0
            for y in s:
                if x != y:
                    if y in adj and x in adj[y]:
                        cnt_in += 1
            if cnt_in < cnt_add:
                add = x
                cnt_add = cnt_in
        assert add > 0
        s.remove(add)
        res.append(add)

    ans += res[len(res)//2]

print(f"Part 2: {ans}")
