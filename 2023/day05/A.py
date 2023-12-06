import sys
from collections import deque

lines = open(sys.argv[1]).readlines()

seeds = list(map(int, lines[0].split(": ")[-1].split()))
print(seeds)

mp = dict()
nxt = dict()

mp["seed"] = dict()
for x in seeds:
    mp["seed"][x] = x

cmp = None
for line in lines[1:]:
    if line == "\n":
        if cmp is not None:
            mp[cmp[1]] = dict()
            for x in mp[cmp[0]]:
                y = mp[cmp[0]][x]
                mp[cmp[1]][y] = y
        cmp = None
    elif cmp is None:
        s, t = line.split()[0].split("-to-")
        nxt[s] = t
        cmp = (s, t)
    else:
        t_range, s_range, sz = list(map(int, line.split()))
        s, t = cmp
        for x in mp[s]:
            if 0 <= x - s_range < sz:
                mp[s][x] = t_range + x - s_range


q = deque()
vis = dict()
vis["seed"] = set()
for x in seeds:
    q.append(("seed", x))
    vis["seed"].add(x)

while q:
    t, x = q.popleft()
    if t == "location":
        continue
    if t not in vis:
        vis[t] = set()

    if x in mp[t]:
        n_x = mp[t][x]
    else:
        n_x = x
    n_t = nxt[t]
    if n_t not in vis:
        vis[n_t] = set()

    if n_x not in vis[n_t]:
        q.append((n_t, n_x))
        vis[n_t].add(n_x)

print(min(vis["location"]))
