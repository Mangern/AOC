import sys


grid = open(sys.argv[1]).read().splitlines()

vis = set()
n = len(grid)
m = len(grid[0])

def dfs(i, j, di, dj):
    while True:
        if i < 0 or i >= n or j < 0 or j >= m:
            return

        vis.add((i,j,di,dj))
        if grid[i][j] != '.':
            break

        i += di
        j += dj

        if (i, j, di, dj) in vis:
            return

    if grid[i][j] == '|':
        if di == 0:
            dfs(i-1, j, -1, 0)
            dfs(i+1, j, +1, 0)
        else:
            dfs(i+di, j, di, dj)
    elif grid[i][j] == '-':
        if dj == 0:
            dfs(i, j-1, 0, -1)
            dfs(i, j+1, 0, +1)
        else:
            dfs(i, j+dj, di, dj)
    elif grid[i][j] == '/':
        # (0, 1) -> (-1, 0), (1, 0) -> (0, -1), (0, -1) -> (1, 0), (-1, 0), (0, 1)
        ndi, ndj = -dj, -di
        dfs(i+ndi, j+ndj, ndi, ndj)
    elif grid[i][j] == '\\':
        # (0, 1) -> (1, 0), (1, 0) -> (0, 1), (0, -1) -> (-1, 0), (-1, 0), (0, -1)
        ndi, ndj = dj, di
        dfs(i+ndi, j+ndj, ndi, ndj)
    else:
        assert False, f"Unknown grid symbol {grid[i][j]}"

dfs(0, 0, 0, 1)
print(len(set((i, j) for i, j, _, __ in vis)))
