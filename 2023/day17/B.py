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
K = 10
# EEESSSWWWNNN
dist = [[[math.inf]*n for i in range(n)] for _ in range(4*K)]

for i in range(2,4):
    dist[K*i+9][0][0] = 0
    heapq.heappush(pq, (0, 0, 0, K*i+9))

while pq:
    d, i, j, dirk = heapq.heappop(pq)

    if dist[dirk][i][j] < d:
        continue

    dir = dirk // K
    
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ni < 0 or ni >= n or nj < 0 or nj >= n:
            continue

        n_dir = base_dir(ni - i, nj - j)
        if n_dir == rev_dir(dir):
            continue

        straight = n_dir == dir

        if not straight and dirk % K < 3:
            continue

        if straight and dirk % K == K - 1:
            continue

        n_dirk = dirk + 1 if straight else n_dir*K
        w = int(grid[ni][nj])
        if d + w < dist[n_dirk][ni][nj]:
            dist[n_dirk][ni][nj] = d + w
            heapq.heappush(pq, (d + w, ni, nj, n_dirk))

print(min(dist[i][n-1][n-1] for i in range(4*K)))
