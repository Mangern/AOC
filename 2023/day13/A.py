import sys

def ref_col(grid, c):
    ct = 0
    for j in range(c - 1, -1, -1):
        if c + ct >= len(grid[0]):
            break
        result = True
        for i in range(len(grid)):
            #print(j, c+ct)
            if grid[i][j] != grid[i][c+ct]:
                result = False
                break
        if not result:
            return False
        ct += 1
    return True

def ref_row(grid, r):
    ct = 0
    for i in range(r-1, -1, -1):
        if r + ct >= len(grid):
            break
        for j in range(len(grid[0])):
            if grid[i][j] != grid[r+ct][j]:
                return False
        ct += 1
    return True


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
