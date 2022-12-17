import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

block = set()

loy = 0

for line in lines:

    path = line.strip().split("->")

    for s,t in zip(path,path[1:]):
        x1,y1 = map(int,s.split(","))
        x2,y2 = map(int,t.split(","))

        loy = max(loy,y1)
        loy = max(loy,y2)

        dx = 0
        dy = 0

        if x1 > x2:
            dx = -1
        elif x1 < x2:
            dx = 1
        elif y1 > y2:
            dy = -1
        elif y1 < y2:
            dy = 1

        while True:
            block.add((x1,y1))
            if x1 == x2 and y1 == y2:
                break
            x1 += dx
            y1 += dy


sx = 500
sy = 0
cnt = 0
while True:
    x = sx
    y = sy

    aby = False
    while True:
        if (x,y+1) not in block:
            if y+1 > loy:
                aby = True
                break
            else:
                y += 1
        elif (x-1,y+1) not in block:
            x -= 1
        elif (x+1,y+1) not in block:
            x += 1
        else:
            break

    if aby:
        break
    block.add((x,y))
    cnt += 1

print(cnt)
