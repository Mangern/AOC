import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

R = 12
G = 13
B = 14

ans = 0
for line in lines:
    gm, cubez = line.strip().split(":")

    gm = int(gm.split()[-1])

    for s in cubez.split(";"):
        r = 0
        g = 0
        b = 0
        for a in s.split(","):
            cnt, name = a.strip().split()
            if name == "red":
                r += int(cnt)
            elif name == "green":
                g += int(cnt)
            elif name == "blue":
                b += int(cnt)
            else:
                print(f"Unknown name {name}")

        if r > R or g > G or b > B:
            break
    else:
        ans += gm

print(ans)
