import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: [int(x) for x in l.strip()], f.readlines()))

n = len(lines)
m = len(lines[0])

visible = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            visible[i][j] = 4 

for i in range(1,n-1):
    mx = lines[i][0]
    for j in range(1,m-1):
        if lines[i][j] > mx:
            visible[i][j] += 1
        mx = max(mx,lines[i][j])

for i in range(1,n-1):
    mx = lines[i][m-1]
    for j in range(m-2,0,-1):
        if lines[i][j] > mx:
            visible[i][j] += 1
        mx = max(mx,lines[i][j])

for j in range(1,m-1):
    mx = lines[0][j]
    for i in range(1,n-1):
        if lines[i][j] > mx:
            visible[i][j] += 1
        mx = max(mx,lines[i][j])

for j in range(1,m-1):
    mx = lines[n-1][j]
    for i in range(n-2,0,-1):
        if lines[i][j] > mx:
            visible[i][j] += 1
        mx = max(mx,lines[i][j])

print(visible)

print(sum(sum(map(lambda b: 1 if b else 0, l)) for l in visible))
