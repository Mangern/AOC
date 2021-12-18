from queue import PriorityQueue

def p1():
    with open("input.txt") as f:
        grid = [[int(c) for c in s.strip()] for s in f.readlines()]

    n = len(grid)
    m = len(grid[0])

    def neighbors(i,j):
        for di,dj in [(0,-1), (1,0), (0,1), (-1,0)]:
            if i+di >= 0 and i + di < n and j+dj >= 0 and j+dj < m:
                yield i+di, j+dj



    INF = 1000000000
    dist = [[INF for j in range(m)] for i in range(n)]

    dist[0][0] = 0

    pq = PriorityQueue()
    pq.put((0,(0,0)))

    while not pq.empty():
        d,(i,j) = pq.get()
        if d > dist[i][j]:
            continue

        for ni,nj in neighbors(i,j):
            if d + grid[ni][nj] < dist[ni][nj]:
                dist[ni][nj] = d + grid[ni][nj]
                pq.put((dist[ni][nj], (ni,nj)))

    print(dist[n-1][m-1])

def p2():
    with open("input.txt") as f:
        init_grid = [[int(c) for c in s.strip()] for s in f.readlines()]

    diff_grid = [[0, 1, 2, 3, 4],
                 [1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 6],
                 [3, 4, 5, 6, 7],
                 [4, 5, 6, 7, 8]]

    n = len(init_grid)
    m = len(init_grid[0])
    grid = [[0 for j in range(m * 5)] for i in range(n * 5)]
    for r5 in range(5):
        for c5 in range(5):
            add = diff_grid[r5][c5]

            for i in range(n):
                for j in range(m):
                    grid[n * r5 + i][m * c5 + j] = (init_grid[i][j] - 1 + add) % 9 + 1

    n *= 5
    m *= 5

    def neighbors(i,j):
        for di,dj in [(0,-1), (1,0), (0,1), (-1,0)]:
            if i+di >= 0 and i + di < n and j+dj >= 0 and j+dj < m:
                yield i+di, j+dj



    INF = 1000000000
    dist = [[INF for j in range(m)] for i in range(n)]

    dist[0][0] = 0

    pq = PriorityQueue()
    pq.put((0,(0,0)))

    while not pq.empty():
        d,(i,j) = pq.get()
        if d > dist[i][j]:
            continue

        for ni,nj in neighbors(i,j):
            if d + grid[ni][nj] < dist[ni][nj]:
                dist[ni][nj] = d + grid[ni][nj]
                pq.put((dist[ni][nj], (ni,nj)))

    print(dist[n-1][m-1])
    pass

p2()
