import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: [int(x) for x in l.strip()], f.readlines()))

n = len(lines)
m = len(lines[0])

visible = [[1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            #visible[i][j] = 4 
            pass

for i in range(1,n-1):
    stk = [[lines[i][0],0]]
    for j in range(1,m-1):
        while len(stk) > 1 and stk[-1][0] < lines[i][j]:
            stk.pop()
        visible[i][j] *= j - stk[-1][1]
        stk.append([lines[i][j],j])

for i in range(1,n-1):
    stk = [[lines[i][m-1],m-1]]
    for j in range(m-2,0,-1):
        while len(stk) > 1 and stk[-1][0] < lines[i][j]:
            stk.pop()

        visible[i][j] *= stk[-1][1] - j
        stk.append([lines[i][j],j])

for j in range(1,m-1):
    stk = [[lines[0][j],0]]
    for i in range(1,n-1):
        while len(stk) > 1 and stk[-1][0] < lines[i][j]:
            stk.pop()

        visible[i][j] *= i - stk[-1][1]
        stk.append([lines[i][j],i])

for j in range(1,m-1):
    stk = [[lines[n-1][j],n-1]]
    for i in range(n-2,0,-1):
        while len(stk) > 1 and stk[-1][0] < lines[i][j]:
            stk.pop()

        visible[i][j] *= stk[-1][1] - i
        stk.append([lines[i][j],i])


print(visible)
print(max(max(l) for l in visible))
