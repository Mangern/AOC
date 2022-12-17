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


toint = dict()
ptr = 0
start = -1
for u in dist:
    toint[u] = ptr
    if (u == "AA"):
        start = ptr
    ptr += 1

print(len(dist))
print(start)

for i in dist:
    print(flow[i])

for u in dist:
    for v in dist:
        print(f"{toint[u]} {toint[v]} {dist[u][v]}")

        
dp = dict()

def calc(key1,key2, t1, t2, mask):
    if (key1,key2,t1,t2,mask) in dp:
        return dp[(key1,key2,t1,t2,mask)]
    if min(t1,t2) >= 26:
        return 0

    ret = 0

    for i in range(m):
        if mask & (1<<i):
            continue
        for j in range(m):
            if j == i:
                continue
            if mask & (1<<j):
                continue

            there1 = t1 + dist[key1][has_pos[i]] + 1
            there2 = t2 + dist[key2][has_pos[j]] + 1

            c = flow[has_pos[i]] * max(0, 26 - there1) + flow[has_pos[j]] * max(0,26 - there2)
            c += calc(has_pos[i], has_pos[j], there1,there2, mask | (1<<i) | (1<<j))
            ret = max(ret,c)

    dp[(key1,key2,t1,t2,mask)] = ret
    return ret

#print(calc("AA","AA",0,0,0))
