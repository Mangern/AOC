from collections import deque
import sys

T_BC = 0
T_FF = 1
T_CN = 2

mp = dict()
tp = dict()
st_i = dict()
ip_c = dict()

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
    mp[mod] = targets

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
            for nt in mp[to]:
                q.append((nxt, to, nt))
    return lo, hi

al = ah = 0
for _ in range(1000):
    lo, hi = simul()
    al += lo
    ah += hi

print(al * ah)
