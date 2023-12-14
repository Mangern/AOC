import sys

def tilt_dir(grid, di, dj):
    n = len(grid)
    m = len(grid[0])

    def send(i, j):
        if grid[i][j] != 'O':
            return

        while 0 <= i+di < n and 0 <= j + dj < m and grid[i+di][j+dj] == '.':
            grid[i+di][j+dj] = 'O'
            grid[i][j] = '.'

            i += di
            j += dj

    ir = range(n) if di <= 0 else range(n-1, -1, -1)
    jr = range(m) if dj <= 0 else range(m-1, -1, -1)
    for i in ir:
        for j in jr:
            send(i,j)

def cycle(grid):
    tilt_dir(grid, -1,  0)
    tilt_dir(grid,  0, -1)
    tilt_dir(grid,  1,  0)
    tilt_dir(grid,  0,  1)

def get_load(grid):
    res = 0
    for i, row in enumerate(grid):
        for c in row:
            if c == 'O':
                res += len(grid) - i
    return res

grid = [
    list(line) 
    for line in open(sys.argv[1]).read()
                                 .splitlines()
]

grid_str = "".join("".join(row) for row in grid)
num_iters = 0
save = {grid_str: 0}

while True:
    cycle(grid)
    num_iters += 1
    grid_str = "".join("".join(row) for row in grid)

    if grid_str in save:
        break

    save[grid_str] = num_iters

goal = 1000000000

P = num_iters - save[grid_str]

rem = (goal - save[grid_str]) % P

for _ in range(rem):
    cycle(grid)

print(get_load(grid))
