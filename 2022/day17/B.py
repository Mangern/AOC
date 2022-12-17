from functools import reduce
from math import log2, ceil
import sys

def main():
    with open(sys.argv[1], "r") as f:
        line = f.readlines()[0].strip()

    m = len(line)
    #mxN = 2022 
    mxN = 1000000000000

    def spawn(i, maxy):
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

    def sim(line,m,mv_ptr, mxN, breaker = True):
        print(f"Simulate {mxN} steps")
        n = 0
        record = dict()
        fst_rec = -1
        start_h = -1
        delta_h = -1
        delta_n = -1
        maxy = 0
        blocked = set()
        while n < mxN:
            curr = spawn(n, maxy)
            down = False
            while True:
                if down:
                    ncurr = list(map(lambda t: (t[0],t[1]-1),curr))
                    if any(pt in blocked or pt[1] <= 0 for pt in ncurr):
                        maxy = reduce(max,map(lambda t:t[1],curr), maxy)
                        blocked |= set(curr)

                        if n % 5 == 0:
                            if mv_ptr in record and fst_rec == -1:
                                fst_rec = mv_ptr
                            elif fst_rec == mv_ptr:
                                delta_h = maxy - record[mv_ptr][0]
                                delta_n = n - record[mv_ptr][1]
                            record[mv_ptr] = (maxy,n)
                        break
                    curr = ncurr
                else:
                    delta = -1 if line[mv_ptr] == "<" else 1
                    mv_ptr = (mv_ptr + 1)%m
                    ncurr = list(map(lambda t: (t[0]+delta,t[1]),curr))
                    if all(pt not in blocked and 1 <= pt[0] <= 7 for pt in ncurr):
                        curr = ncurr
                down = not down

            if delta_h != -1 and breaker:
                break
            n += 1
        print(f"Simulated {n} out of {mxN} steps {'because im lazy' if n < mxN else ''}")
        return (maxy, n, delta_h, delta_n, fst_rec)

    #draw()
    maxy,n,delta_h,delta_n,fst_ptr = sim(line, m, 0,mxN, True)
    start_h = maxy
    if delta_h != -1:
        start_n = n
        x = (mxN - n + delta_n - 1) // delta_n
        n += (x - 1) * delta_n
        maxy += (x - 1) * delta_h

        nxy, _, _, _, _ = sim(line, m, 0, start_n + mxN - n, False) 
        nxy -= start_h
        maxy += nxy
    print(maxy)

if __name__ == "__main__":
    main()
