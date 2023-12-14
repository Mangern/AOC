import sys

def tilt_north(grid):
    n = len(grid)
    m = len(grid[0])

    def send_up(i, j):
        if grid[i][j] != 'O':
            return

        while i > 0 and grid[i-1][j] == '.':
            grid[i-1][j] = 'O'
            grid[i][j] = '.'
            i -= 1

    for i in range(n):
        for j in range(m):
            send_up(i,j)

grid = [
    list(line) 
    for line in open(sys.argv[1]).read()
                                 .splitlines()
]

tilt_north(grid)

ans = 0
for i, row in enumerate(grid):
    for c in row:
        if c == 'O':
            ans += len(grid) - i

print(ans)
