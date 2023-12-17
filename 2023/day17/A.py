import math
import sys
import heapq

def base_dir(di, dj):
    if dj == 1:
        return 0
    if di == 1:
        return 1
    if dj == -1:
        return 2
    if di == -1:
        return 3
    assert False

def rev_dir(dir):
    return (dir + 2)%4
    

grid = open(sys.argv[1]).read().splitlines()

n = len(grid)


pq = []
# EEESSSWWWNNN
dist = [[[math.inf]*n for i in range(n)] for _ in range(12)]

for i in range(2,4):
    dist[3*i][0][0] = 0
    heapq.heappush(pq, (0, 0, 0, 3*i))

while pq:
    d, i, j, dirk = heapq.heappop(pq)

    if dist[dirk][i][j] < d:
        continue

    dir = dirk // 3
    
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ni < 0 or ni >= n or nj < 0 or nj >= n:
            continue

        n_dir = base_dir(ni - i, nj - j)
        if n_dir == rev_dir(dir):
            continue
        inc = 1 if n_dir == dir else 0
        if inc and (dirk % 3 == 2):
            continue

        n_dirk = dirk + inc if inc else n_dir*3
        w = int(grid[ni][nj])
        if d + w < dist[n_dirk][ni][nj]:
            dist[n_dirk][ni][nj] = d + w
            heapq.heappush(pq, (d + w, ni, nj, n_dirk))

print(min(dist[i][n-1][n-1] for i in range(12)))


