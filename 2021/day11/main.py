def p1():
    with open("input.txt") as f:
        grid = [[int(c) for c in line.strip()] for line in f.readlines()]

    n = len(grid)
    m = len(grid[0])

    def neighbors(i,j):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if i+di < 0 or i+di >= n or j + dj < 0 or j + dj >= m or (i,j) == (i+di, j+dj):
                    continue
                yield i+di,j+dj

    ans = 0
    for step in range(100):
        # inc 1
        grid = list(map(lambda row: list(map(lambda el: el + 1, row)), grid))
        flash = {(i,j) for j in range(m) for i in range(n) if grid[i][j] > 9}

        vis = {t for t in flash} 

        while len(flash) > 0:
            ans += len(flash)

            for i,j in flash:
                for ni,nj in neighbors(i,j):
                    grid[ni][nj] += 1

            flash.clear()
            flash = {(i,j) for j in range(m) for i in range(n) if grid[i][j] > 9 and (i,j) not in vis}
            vis = vis.union(flash)

        for i,j in vis:
            grid[i][j] = 0

    print(ans)

def p2():
    with open("input.txt") as f:
        grid = [[int(c) for c in line.strip()] for line in f.readlines()]

    n = len(grid)
    m = len(grid[0])

    def neighbors(i,j):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if i+di < 0 or i+di >= n or j + dj < 0 or j + dj >= m or (i,j) == (i+di, j+dj):
                    continue
                yield i+di,j+dj

    ans = 0
    step = 1
    while True: 
        # inc 1
        grid = list(map(lambda row: list(map(lambda el: el + 1, row)), grid))
        flash = {(i,j) for j in range(m) for i in range(n) if grid[i][j] > 9}

        vis = {t for t in flash} 


        while len(flash) > 0:
            ans += len(flash)

            for i,j in flash:
                for ni,nj in neighbors(i,j):
                    grid[ni][nj] += 1

            flash.clear()
            flash = {(i,j) for j in range(m) for i in range(n) if grid[i][j] > 9 and (i,j) not in vis}
            vis = vis.union(flash)

        for i,j in vis:
            grid[i][j] = 0
        if len(vis) == n * m:
            print(step)
            break

        step += 1



p2()
