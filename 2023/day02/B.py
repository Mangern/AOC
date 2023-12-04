import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
ans = 0
for line in lines:
    gm, cubez = line.strip().split(":")

    gm = int(gm.split()[-1])

    r = 0
    g = 0
    b = 0
    for s in cubez.split(";"):
        for a in s.split(","):
            cnt, name = a.strip().split()
            if name == "red":
                r = max(r, int(cnt))
            elif name == "green":
                g = max(g, int(cnt))
            elif name == "blue":
                b = max(b, int(cnt))
            else:
                print(f"Unknown name {name}")

    ans += r * g * b

print(ans)

