import sys

with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: l.split(),f.readlines()))

grid = [['.' for j in range(40)] for i in range(6)] 

r = 0
c = 0


x = 1

def nxt_pos():
    global r
    global c
    c += 1
    if c == 40:
        c = 0
        r += 1

for line in lines:
    if line[0] == "addx":
        if abs(c-x) <= 1:
            grid[r][c] = '#'
        nxt_pos()
        if abs(c-x) <= 1:
            grid[r][c] = '#'
        x += int(line[1])
        nxt_pos()
    else:
        if abs(c-x) <= 1:
            grid[r][c] = '#'
        nxt_pos()

for g in grid:
    print("".join(g))
