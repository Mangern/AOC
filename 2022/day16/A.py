from itertools import permutations
import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: l.split(), f.readlines()))

flow = dict()
adj = dict()

has_pos = []

for line in lines:
    key = line[1]
    flow[key] = int(line[4][5:-1])

    if flow[key] > 0:
        has_pos.append(key)

    if key not in adj:
        adj[key] = []

    for valc in line[9:]:
        nxt = valc
        if valc != line[-1]:
            nxt = valc[:-1]

        adj[key].append(nxt)


m = len(has_pos)
dist = dict()

for i in adj:
    dist[i] = dict()
    dist[i][i] = 0

for i in adj:
    for j in adj[i]:
        dist[i][j] = 1

for k in adj:
    for i in adj:
        for j in adj:
            if i == j:
                continue
            if k in dist[i] and j in dist[k]:
                if j not in dist[i]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


dp = dict()

def calc(key, t, mask):
    if (key,t,mask) in dp:
        return dp[(key,t,mask)]
    if t >= 30:
        return 0

    ret = 0

    for i in range(m):
        if mask & (1<<i):
            continue
        there = t + dist[key][has_pos[i]] + 1
        c = flow[has_pos[i]] * max(0, 30 - there) + calc(has_pos[i], there, mask | (1<<i))
        ret = max(ret,c)

    dp[(key,t,mask)] = ret
    return ret

print(calc("AA",0,0))
