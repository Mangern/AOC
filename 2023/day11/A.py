from itertools import product
import sys

grid = open(sys.argv[1]).read().splitlines()

erow, ecol = set(), set()
n = len(grid)
m = len(grid[0])

for i, row in enumerate(grid):
    if all(c == '.' for c in row):
        erow.add(i)

for j in range(m):
    if all(grid[i][j] == '.' for i in range(n)):
        ecol.add(j)


pos = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            pos.append((i, j))

ans = 0
for (x1, y1), (x2, y2) in product(pos, pos):
    if (x1, y1) == (x2, y2):
        continue
    ans += abs(x2 - x1) + abs(y2 - y1)
    for z in erow:
        if min(x1,x2) < z < max(x1, x2):
            ans += 1
    for z in ecol:
        if min(y1,y2) < z < max(y1, y2):
            ans += 1

print(ans >> 1)
