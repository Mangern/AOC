from sys import stdin

grid = [list(line.strip()) for line in stdin]

n = len(grid)
m = len(grid[0])

si = None
sj = None

for i in range(n):
    for j in range(m):
        if grid[i][j] == '^':
            si = i
            sj = j

ans = [[grid[i][j] for j in range(m)] for i in range(n)]

grid[si][sj] = '.'
ans[si][sj] = 'X'

dir = [-1, 0]

def rturn():
    global dir
    if dir[0] == -1:
        dir = [0, 1]
    elif dir[0] == 0 and dir[1] == 1:
        dir = [1, 0]
    elif dir[0] == 1:
        dir = [0, -1]
    else:
        dir = [-1, 0]

while True:
    ni = si + dir[0]
    nj = sj + dir[1]

    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        break

    if grid[ni][nj] == '#':
        rturn()
        continue
    ans[ni][nj] = 'X'
    si = ni
    sj = nj

cnt = 0
for l in ans:
    cnt += sum(1 for c in l if c == 'X')

print(cnt)
