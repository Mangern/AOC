from itertools import groupby
def p1():
    with open("input.txt") as f:
        points, folds = [[s.strip() for s in y] for x,y in groupby(f.readlines(), lambda line: line == "\n") if not x]

    grid = {(int(x), int(y)) for x,y in [s.split(",") for s in points]}

    chop = len("fold along ")

    axis = folds[0][chop:chop+1]
    chop = len("fold along .=")

    fold = int(folds[0][chop:])

    if axis == 'x':
        grid = {(x,y) if x < fold else (2*fold-x, y) for x,y in grid}
        pass
    else:
        # (x0,y0) -> (x0, 2*fold -y0) if y0 > fold

        grid = {(x,y) if y < fold else (x,2*fold - y) for x,y in grid}

    print(len(grid))

def p2():
    with open("input.txt") as f:
        points, folds = [[s.strip() for s in y] for x,y in groupby(f.readlines(), lambda line: line == "\n") if not x]

    grid = {(int(x), int(y)) for x,y in [s.split(",") for s in points]}

    for line in folds:
        chop = len("fold along ")

        axis = line[chop:chop+1]
        chop = len("fold along .=")

        fold = int(line[chop:])

        if axis == 'x':
            grid = {(x,y) if x < fold else (2*fold-x, y) for x,y in grid}
            pass
        else:
            # (x0,y0) -> (x0, 2*fold -y0) if y0 > fold

            grid = {(x,y) if y < fold else (x,2*fold - y) for x,y in grid}


    w = max({x for x,y in grid}) + 1
    h = max({y for x,y in grid}) + 1


    ansgrid = [["." for x in range(w)] for y in range(h)]

    for x,y in grid:
        ansgrid[y][x] = "#"

    for line in ansgrid:
        print("".join(line))
p2()
