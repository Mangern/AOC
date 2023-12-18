import sys
from collections import deque

tr = set([(0,0)])

posi = posj = 0

for line in open(sys.argv[1]).readlines():
    dir, step = line.split()[:2]
    step = int(step)
    di = 1 if dir == 'D' else (-1 if dir == 'U' else 0)
    dj = 1 if dir == 'R' else (-1 if dir == 'L' else 0)

    for _ in range(step):
        posi += di
        posj += dj

        tr.add((posi, posj))

mn_i = min(i for i, j in tr)
mx_i = max(i for i, j in tr)
mn_j = min(j for i, j in tr)
mx_j = max(j for i, j in tr)

tr = set([(i-mn_i, j - mn_j) for i, j in tr])

n = mx_i - mn_i + 1
m = mx_j - mn_j + 1

grid = [['.' if (i, j) not in tr else '#' for j in range(m)] for i in range(n)]
q = deque()

for j in range(m):
    if grid[0][j] == '#' and grid[1][j] != '#':
        grid[1][j] = '#'
        q.append((1,j))

while q:
    i, j = q.popleft()
    for (ni, nj) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        if grid[ni][nj] == '.':
            grid[ni][nj] = '#'
            q.append((ni,nj))

#print("\n".join("".join(row) for row in grid))

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            ans += 1
print(ans)
