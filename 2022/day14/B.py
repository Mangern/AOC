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


loy += 2
sx = 500
sy = 0
cnt = 0

def check(x,y):
    global block
    global loy

    if y >= loy:
        return False
    return (x,y) not in block

while check(sx,sy):
    x = sx
    y = sy
    while True:
        if check(x,y+1):
            y += 1
        elif check(x-1,y+1):
            x -= 1
            y += 1
        elif check(x+1,y+1):
            x += 1
            y += 1
        else:
            break

    block.add((x,y))
    cnt += 1

print(cnt)
