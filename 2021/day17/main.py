def p1():
    """ stupid sol (as always) """
    with open("input.txt") as f:
        line = f.read().strip()

    (x0, x1), (y0, y1) = [list(map(int, s.split(".."))) for s in line[15:].split(", y=")]

    ans = 0

    for xv0 in range(1,500):
        for yv0 in range(500):
            xv,yv = xv0, yv0
            x,y = 0,0

            max_y = 0
            success = False

            while True:
                x += xv
                y += yv

                max_y = max(max_y, y)

                if x0 <= x <= x1 and y0 <= y <= y1:
                    success = True
                    break

                if x > x1 or y < y0:
                    break

                if xv > 0:
                    xv -= 1

                yv -= 1

            if success:
                ans = max(ans, max_y)

    print(ans)

def p2():
    """ stupid sol (as always) """
    with open("input.txt") as f:
        line = f.read().strip()

    (x0, x1), (y0, y1) = [list(map(int, s.split(".."))) for s in line[15:].split(", y=")]

    ans = 0

    for xv0 in range(1,500):
        for yv0 in range(-200, 500):
            xv,yv = xv0, yv0
            x,y = 0,0

            max_y = 0
            success = False

            while True:
                x += xv
                y += yv

                max_y = max(max_y, y)

                if x0 <= x <= x1 and y0 <= y <= y1:
                    success = True
                    break

                if x > x1 or y < y0:
                    break

                if xv > 0:
                    xv -= 1

                yv -= 1

            if success:
                ans += 1

    print(ans)
    pass
p2()
