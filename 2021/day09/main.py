def p1():
    with open("input.txt") as f:
        grid = [[int(x) for x in list(line.strip())] for line in f.readlines()]

    n = len(grid)
    m = len(grid[0])

    def neighbors(i,j):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if not any([di==0, dj==0]):
                    continue
                if i + di < 0 or i + di >= n or j + dj < 0 or j + dj >= m or (di == 0 and dj == 0):
                    continue
                yield grid[i+di][j+dj]


    ans = sum([grid[i][j] + 1 for i in range(n) for j in range(m) if all([neigh > grid[i][j] for neigh in neighbors(i,j)])])
    
    print(ans)


def p2():
    with open("input.txt") as f:
        grid = [[int(x) for x in list(line.strip())] for line in f.readlines()]

    n = len(grid)
    m = len(grid[0])

    def neighbors(i,j):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if not any([di==0, dj==0]):
                    continue
                if i + di < 0 or i + di >= n or j + dj < 0 or j + dj >= m or (di == 0 and dj == 0):
                    continue
                yield i+di,j+dj


    lows = [(i,j) for i in range(n) for j in range(m) if all([grid[ni][nj] > grid[i][j] for ni,nj in neighbors(i,j)])]

    basin_id = [[-1 for j in range(m)] for i in range(n)]

    def dfs(i,j, idx):
        if grid[i][j] == 9:
            return
        basin_id[i][j] = idx

        for ni,nj in neighbors(i,j):
            if grid[ni][nj] > grid[i][j]:
                dfs(ni,nj, idx)


    for idx, p in enumerate(lows):
        dfs(*p, idx)

    sz = {}

    for i in range(n):
        for j in range(m):
            idx = basin_id[i][j]

            if idx != -1:
                if idx in sz:
                    sz[idx] += 1
                else:
                    sz[idx] = 1

    vals = [sz[key] for key in sz]

    vals.sort()


    ans = vals[-1] * vals[-2] * vals[-3]
    print(ans)

    

p2()
