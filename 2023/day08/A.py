from collections import deque
import sys
import math

with open(sys.argv[1]) as f:
    lines = f.readlines()

insr = lines[0].strip()

k = len(insr)

adj = dict()

for line in lines[2:]:
    u, rest = line.strip().split(" = ")
    l, r = rest[1:-1].split(", ")
    adj[u] = list()

    for i in range(k):
        if insr[i] == "L":
            adj[u].append(l)
        else:
            adj[u].append(r)

q = deque()
q.append(("AAA", 0))
dist = dict()
dist[("AAA", 0)] = 0

while q:
    u, i = q.popleft()

    v = adj[u][i]
    j = (i + 1)%k

    if (v, j) not in dist:
        dist[(v, j)] = dist[(u, i)] + 1
        q.append((v, j))

ans = math.inf
for i in range(k):
    if ("ZZZ", i) in dist:
        ans = min(ans, dist[("ZZZ", i)])
print(ans)

