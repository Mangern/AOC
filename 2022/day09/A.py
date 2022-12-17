import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

vis = set([(0,0)])

h_p = (0,0)
t_p = (0,0)

direc = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

for line in lines:
    cmd, val = line.split()

    val = int(val)
    dr = direc[cmd]

    for _ in range(val):
        h_p = (h_p[0] + dr[0], h_p[1] + dr[1])

        if h_p[0] == t_p[0]:
            if h_p[1] - t_p[1] > 1:
                t_p = (t_p[0], t_p[1] + 1)
            elif t_p[1] - h_p[1] > 1:
                t_p = (t_p[0], t_p[1] - 1)
        elif h_p[1] == t_p[1]:
            if h_p[0] - t_p[0] > 1:
                t_p = (t_p[0] + 1, t_p[1])
            elif t_p[0] - h_p[0] > 1:
                t_p = (t_p[0] - 1, t_p[1])
        elif abs(h_p[0] - t_p[0]) + abs(h_p[1] - t_p[1]) > 2:
            d_x = 1 if h_p[0] > t_p[0] else -1
            d_y = 1 if h_p[1] > t_p[1] else -1
            t_p = (t_p[0] + d_x, t_p[1] + d_y)
        vis.add(t_p)

print(len(vis))

