import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

vis = set([(0,0)])

h_p = (0,0)
t_ps = [(0,0) for _ in range(9)]

direc = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

for line in lines:
    cmd, val = line.split()

    val = int(val)
    dr = direc[cmd]

    for _ in range(val):
        h_p = (h_p[0] + dr[0], h_p[1] + dr[1])

        ptr = h_p

        i = 0

        while i < len(t_ps):
            t_p = t_ps[i]
            if ptr[0] == t_p[0]:
                if ptr[1] - t_p[1] > 1:
                    t_p = (t_p[0], t_p[1] + 1)
                elif t_p[1] - ptr[1] > 1:
                    t_p = (t_p[0], t_p[1] - 1)
            elif ptr[1] == t_p[1]:
                if ptr[0] - t_p[0] > 1:
                    t_p = (t_p[0] + 1, t_p[1])
                elif t_p[0] - ptr[0] > 1:
                    t_p = (t_p[0] - 1, t_p[1])
            elif abs(ptr[0] - t_p[0]) + abs(ptr[1] - t_p[1]) > 2:
                d_x = 1 if ptr[0] > t_p[0] else -1
                d_y = 1 if ptr[1] > t_p[1] else -1
                t_p = (t_p[0] + d_x, t_p[1] + d_y)

            t_ps[i] = t_p
            ptr = t_ps[i]
            i += 1

        vis.add(t_ps[-1])

print(len(vis))

