from sys import stdin
from time import sleep

n = 103
m = 101

pos = []

for line in stdin:
    ps, vs = line.split()
    ps = ps[2:]
    vs = vs[2:]

    px, py = map(int, ps.split(","))
    vx, vy = map(int, vs.split(","))
    px = (px + 128 * vx) % m
    py = (py + 128 * vy) % n
    pos.append([px, py, vx, vy])


def printgrid(grid):
    print("\n".join("".join(row) for row in grid))
    print()


step = 128
while True:
    grid = [['.' for _ in range(m)] for _ in range(n)]
    for px, py, _, _ in pos:
        grid[py][px] = '*'

    for i in range(len(pos)):
        px, py, vx, vy = pos[i]
        px = (px + 206 * vx) % m
        py = (py + 206 * vy) % n
        pos[i][0] = px
        pos[i][1] = py

    print(step)
    step += 206
    printgrid(grid)
    sleep(0.2)
