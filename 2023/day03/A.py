import sys

with open(sys.argv[1], "r") as f:
    grid = [line.strip() for line in f.readlines()]

n = len(grid)
m = len(grid[0])

def issym(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    return (not grid[i][j].isdigit()) and grid[i][j] != "."

def check_num(i, j):
    part = False
    if issym(i-1, j-1) or issym(i, j-1) or issym(i+1, j-1):
        part = True

    num = 0
    k = j
    while k < m and grid[i][k].isdigit():
        num *= 10
        num += int(grid[i][k])
        if issym(i-1, k) or issym(i+1, k):
            part = True
        k += 1

    if issym(i-1, k) or issym(i, k) or issym(i+1, k):
        part = True

    return num if part else 0

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j].isdigit() and (j == 0 or not grid[i][j-1].isdigit()):
            ans += check_num(i, j)

print(ans)
