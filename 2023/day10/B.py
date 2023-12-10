import sys
from itertools import chain
from collections import deque
sys.setrecursionlimit(100000)

directions = {
    "-": {
        (0, 1): (0, 1),
        (0,-1): (0,-1)
    },
    "|": {
        (1, 0): (1, 0),
        (-1,0): (-1,0)
    },
    "L": {
        (1, 0): (0, 1),
        (0,-1): (-1,0)
    },
    "J": {
        (1, 0): (0,-1),
        (0, 1): (-1,0)
    },
    "7": {
        (-1,0): (0,-1),
        (0, 1): (1, 0)
    },
    "F": {
        (-1,0): (0, 1),
        (0,-1): (1, 0),
    },
    ".": {}
}

def search(pi, pj, i, j, grid, vis):
    vis.add((i, j))
    di, dj = i - pi, j - pj
    c = grid[i][j]

    if (di, dj) not in directions[c]:
        return None
    ndi, ndj = directions[c][(di, dj)]
    ni, nj = i + ndi, j + ndj
    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
        return None

    if grid[ni][nj] == "S":
        return [(i, j)]

    if (ni, nj) in vis:
        return None

    path = search(i, j, ni, nj, grid, vis)
    if path is None:
        return None
    path.append((i, j))
    return path

with open(sys.argv[1]) as f:
    grid = [line.strip() for line in f.readlines()]


n = len(grid)
m = len(grid[0])

si = None
sj = None
path = None

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            si = i
            sj = j
            break
    if si is not None:
        break

for ni, nj in [(si-1, sj), (si+1, sj), (si, sj-1), (si, sj+1)]:
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        continue

    vis = set([(si, sj)])
    path = search(si, sj, ni, nj, grid, vis)
    if path is not None:
        path.insert(0, (si,sj))
        break

tg = [[0]*2*m for _ in range(2*n)]

for step, (i, j) in enumerate(path):
    tg[2*i][2*j] = 1

for (i, j), (ni, nj) in zip(path, chain(path[1:], path[:1])):
    mi, mj = (i+ni), (j+nj)
    tg[mi][mj] = 1


q = deque()
for i in range(2 * n):
    for j in range(2 * m):
        if (i == 0 or j == 0 or i == 2*n - 1 or j == 2*m - 1) and tg[i][j] == 0:
            tg[i][j] = 2
            q.append((i, j))

while len(q):
    i, j = q.popleft()

    for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if ni < 0 or ni >= 2*n or nj < 0 or nj >= 2 * m:
            continue
        if tg[ni][nj]:
            continue
        tg[ni][nj] = 2
        q.append((ni,nj))

res = [[0]*m for _ in range(n)]

for i in range(2*n):
    for j in range(2*m):
        if not res[i//2][j//2]:
            res[i//2][j//2] = tg[i][j]

cnt = sum(1 for row in res for x in row if not x)
print(cnt)
