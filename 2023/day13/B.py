import sys

def ref_col(grid, c):
    ct = 0
    cnt = 0
    for j in range(c - 1, -1, -1):
        if c + ct >= len(grid[0]):
            break
        for i in range(len(grid)):
            #print(j, c+ct)
            if grid[i][j] != grid[i][c+ct]:
                cnt += 1
        if cnt > 1:
            return False
        ct += 1
    return cnt == 1

def ref_row(grid, r):
    ct = 0
    cnt = 0
    for i in range(r-1, -1, -1):
        if r + ct >= len(grid):
            break
        for j in range(len(grid[0])):
            if grid[i][j] != grid[r+ct][j]:
                cnt += 1
        if cnt > 1:
            return False
        ct += 1
    return cnt == 1


def solve(grid):
    grid = [s for s in grid if len(s)]
    n = len(grid)
    m = len(grid[0])

    for i in range(1, m):
        if ref_col(grid, i):
            return i

    for i in range(1, n):
        if ref_row(grid, i):
            return 100 * i


grids = open(sys.argv[1]).read().split("\n\n")

ans = 0
for grid in grids:
    a = grid.split("\n")
    ans += solve(a)

print(ans)

