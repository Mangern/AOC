import sys

with open(sys.argv[1], "r") as f:
    grid = [line.strip() for line in f.readlines()]

n = len(grid)
m = len(grid[0])

def gear_id(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if grid[i][j] == '*':
        return i * n + j + 1
    return 0

def check_num(i, j):
    gear = gear_id(i-1, j-1) or gear_id(i, j-1) or gear_id(i+1, j-1)

    num = 0
    k = j
    gears = set([gear])
    while k < m and grid[i][k].isdigit():
        num *= 10
        num += int(grid[i][k])
        gears.add(gear_id(i-1, k))
        gears.add(gear_id(i+1, k))
        k += 1

    gears.add(gear_id(i-1, k))
    gears.add(gear_id(i, k))
    gears.add(gear_id(i+1, k))

    return num, gears

ans = 0
gs = dict()
for i in range(n):
    for j in range(m):
        if grid[i][j].isdigit() and (j == 0 or not grid[i][j-1].isdigit()):
            num, gears = check_num(i, j)
            for g in gears:
                if g:
                    if g not in gs:
                        gs[g] = []
                    gs[g].append(num)

for g in gs:
    if len(gs[g]) == 2:
        ans += gs[g][0] * gs[g][1]

print(ans)
