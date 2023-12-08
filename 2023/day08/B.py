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

dist = dict()
al = []
zl = dict()
zs = dict()
for s in adj:
    if s[-1] == "A":
        al.append(s)
        zl[s] = []
        zs[s] = []

for s in al:
    u = s
    i = 0
    while True:
        if u[-1] == "Z":
            found = False
            for j, v in zip(zl[s], zs[s]):
                if v == u:
                    found = True
                    break
            zs[s].append(u)
            if found:
                zl[s].append(i - zl[s][-1])
                break
            zl[s].append(i)
        u = adj[u][i%k]
        i += 1

def gcd(a, b):
    return gcd(b, a%b) if b else a

def lcm(a, b):
    l = a * b
    return l // gcd(a, b)

a = [zl[s][-1] for s in al]

ans = lcm(a[0], a[1])

for x in a:
    ans = lcm(ans, x)
print(ans)
