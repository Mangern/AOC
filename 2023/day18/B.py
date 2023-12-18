import sys
from collections import deque

pts = [(0,0)]

perim = 0
pi = pj = 0
for line in open(sys.argv[1]).readlines():
    s = line.split()[-1][2:-1]

    step = int(s[:5], 16)
    di, dj = [(0,1),(1,0),(0,-1),(-1,0)][int(s[-1])]

    pi += di * step
    pj += dj * step
    pts.append((pi, pj))
    perim += step


sm = 0

pts.append(pts[1])
for i in range(len(pts) - 1):
    sm += (pts[i][0] + pts[i+1][0]) * (pts[i][1] - pts[i+1][1])

"""
Have to add perimeter + 2 because the area we now have
calculated is the area where the 'trench' is half of its actual width
Adding the half the perimeter works nicely because for every corner
we undercount (the convex corners), there is a corner where we overcount (the concave(?) corners)
Except for 4 convex corners, which in total contribute with 1 full square to the full extra perimeter
"""
sm += perim + 2
sm >>= 1
print(sm)
