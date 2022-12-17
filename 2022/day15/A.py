import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

lines = list(map(lambda l: l.split()[2:],lines))

ay = 2000000
mnx = 10000000000000000000
mxx = -1000000000000000000

close = []
is_bec = set()

for line in lines:
    x1 = int(line[0][2:-1])
    y1 = int(line[1][2:-1])

    x2 = int(line[6][2:-1])
    y2 = int(line[7][2:])

    is_bec.add((x2,y2))

    dst = abs(x1-x2)+abs(y1-y2)
    close.append(((x1,y1),dst))
    mnx = min(mnx,x1-dst)
    mxx = max(mxx,x1+dst)

print(mnx,mxx)

ans = 0
for x in range(mnx,mxx+1):
    if (x,ay) in is_bec:
        continue
    inv = False
    for tup in close:
        x1,y1 = tup[0]
        if abs(x-x1)+abs(ay-y1) <= tup[1]:
            inv = True
            break
    if inv:
        ans += 1

print(ans)

