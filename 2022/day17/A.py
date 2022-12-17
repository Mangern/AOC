import sys

def main():
    with open(sys.argv[1], "r") as f:
        line = f.readlines()[0].strip()

    maxy = 0
    blocked = set()
    n = 0
    m = len(line)
    mxN = 2022 
    mv_ptr = 0

    def spawn(i):
        i %= 5
        if i == 0:
            return [(3,maxy+4),(4,maxy+4),(5,maxy+4),(6,maxy+4)]
        if i == 1:
            return [(4,maxy+4),(3,maxy+5),(4,maxy+5),(5,maxy+5),(4,maxy+6)]
        if i == 2:
            return [(3,maxy+4),(4,maxy+4),(5,maxy+4),(5,maxy+5),(5,maxy+6)]
        if i == 3:
            return [(3,maxy+4),(3,maxy+5),(3,maxy+6),(3,maxy+7)]
        if i == 4:
            return [(3,maxy+4),(4,maxy+4),(3,maxy+5),(4,maxy+5)]
        assert False

    def draw():
        for y in range(maxy,0,-1):
            s = ""
            for x in range(1,8):
                if (x,y) in blocked:
                    s += "#"
                else:
                    s += "."
            print(s)
        print()

    while n < mxN:
        curr = spawn(n)
        down = False
        while True:
            if down:
                ncurr = []
                for pt in curr:
                    ncurr.append((pt[0],pt[1] - 1))
                stop = False
                for pt in ncurr:
                    if pt in blocked or pt[1] <= 0:
                        stop = True
                        break

                if stop:
                    for pt in curr:
                        blocked.add(pt)
                        maxy = max(maxy,pt[1])
                    break
                curr = ncurr
            else:
                delta = 0
                if line[mv_ptr] == "<":
                    delta = -1
                else:
                    delta = 1

                mv_ptr += 1
                mv_ptr %= m
                ncurr = []
                for pt in curr:
                    ncurr.append((pt[0] + delta, pt[1]))
                stop = False
                for pt in ncurr:
                    if pt in blocked or pt[0] <= 0 or pt[0] >= 8:
                        stop = True
                        break

                if not stop:
                    curr = ncurr

            down = not down
        #draw()
        n += 1
    print(maxy)


if __name__ == "__main__":
    main()
