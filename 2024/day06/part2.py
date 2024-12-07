from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**8)

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

ans = [[[] for j in range(m)] for i in range(n)]

grid[si][sj] = '.'
osi = si
osj = sj

dir = (-1, 0)

def rturn(dir):
    if dir[0] == -1:
        dir = (0, 1)
    elif dir[0] == 0 and dir[1] == 1:
        dir = (1, 0)
    elif dir[0] == 1:
        dir = (0, -1)
    else:
        dir = (-1, 0)
    return dir

def cl_dfs(i, j, dir):
    if (dir[0], dir[1]) in ans[i][j]:
        return True

    ans[i][j].append((dir[0], dir[1]))

    ni = i + dir[0]
    nj = j + dir[1]

    ret = False
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        ret = False
    else:
        if grid[ni][nj] == '#':
            if cl_dfs(i, j, rturn(dir)):
                ret = True
        else:
            if cl_dfs(ni, nj, dir):
                ret = True
    ans[i][j].pop()
    return ret


def causeloop(i, j):
    ni = i + dir[0]
    nj = j + dir[1]

    if grid[ni][nj] == '#':
        return False

    grid[ni][nj] = '#'

    ret = False
    if cl_dfs(i, j, rturn(dir)):
        ret = True

    grid[ni][nj] = '.'
    return ret

obs = set()
ilg = set()
while True:
    ni = si + dir[0]
    nj = sj + dir[1]

    ans[si][sj].append((dir[0], dir[1]))

    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        break

    if (ni, nj) not in ilg:
        if causeloop(si, sj):
            obs.add((ni,nj))
        else:
            ilg.add((ni, nj))

    if grid[ni][nj] == '#':
        dir = rturn(dir)
        continue
    si = ni
    sj = nj

if (osi, osj) in obs:
    obs.remove((osi, osj))

print(len(obs))

for i, j in obs:
    grid[i][j] = 'O'
