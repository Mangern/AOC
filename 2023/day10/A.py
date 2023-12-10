import sys
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

print(max(min(i, len(path) - i) for i in range(len(path))))
tg = [["."]*m for _ in range(n)]

for step, (i, j) in enumerate(path):
    tg[i][j] = str(min(step, len(path) - step))

#print("\n".join("".join(row) for row in tg))
