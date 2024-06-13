from collections import deque
import sys

T_BC = 0
T_FF = 1
T_CN = 2

mp = dict()
tp = dict()
st_i = dict()
ip_c = dict()
adj = dict()
per = dict()

with open(sys.argv[1]) as f:
    lines = f.readlines()



for line in lines:
    mod, targets = map(lambda s: s.strip(), line.split(" -> "))
    targets = targets.split(", ")
    if mod == "broadcaster":
        tp[mod] = T_BC
    elif mod[0] == '%':
        tp[mod[1:]] = T_FF 
        mod = mod[1:]
        st_i[mod] = 0
    else:
        tp[mod[1:]] = T_CN 
        mod = mod[1:]
        ip_c[mod] = dict()
        st_i[mod] = 0
    mp[mod] = targets
    for t in targets:
        if t not in adj:
            adj[t] = []
        adj[t].append(mod)

for start in mp:
    for goal in mp[start]:
        if goal in tp and tp[goal] == T_CN:
            ip_c[goal][start] = 0

def simul():
    q = deque()
    lo = 1
    hi = 0
    for t in mp["broadcaster"]:
        q.append((0, "broadcaster", t))

    while len(q):
        sign, fr, to = q.popleft()
        #print(f"{fr} --{sign}--> {to}")
        if sign == 0:
            lo += 1
        else:
            hi += 1
        if to not in mp:
            continue

        if tp[to] == T_FF:
            if sign == 1:
                pass
            else:
                st_i[to] = 1 - st_i[to]
                for nt in mp[to]:
                    q.append((st_i[to], to, nt))
        else:
            ip_c[to][fr] = sign
            nxt = 1 - int(all(y for x, y in ip_c[to].items()))
            st_i[to] = nxt
            for nt in mp[to]:
                q.append((nxt, to, nt))
    return lo, hi


q = deque()
per["broadcaster"] = 0

q.append("broadcaster")

while len(q):
    u = q.popleft()
    if u not in mp:
        continue
    for v in mp[u]:
        if tp[v] == T_CN:
            continue
        if v not in per:
            per[v] = per[u] + 1
            q.append(v)

zk = dict()
ok = dict()
sample = ["bh", "tp", "fq", "nm", "xp"]
for t in sample:
    zk[t] = 0
    ok[t] = 0

prt = set()
for _ in range(200):
    for t in sample:
        if t in prt:
            continue
        if st_i[t] == 0:
            zk[t] += 1
        else:
            ok[t] += 1
        if zk[t] == ok[t]:
            print(t, per[t], zk[t] + ok[t])
            prt.add(t)
    simul()

def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

ans = 1

for t in ["pn", "vd", "th", "fz"]:
    joker = [per[s] for s in adj[t] if s in per]
    print(sorted(joker))
    nm = 0
    for x in joker:
        nm |= (1<<(x - 1))
    ans = (ans * nm)

print(ans)

# 250924073918341
# 349062127155280
