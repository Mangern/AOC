import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

lines = list(map(lambda l: l.split()[2:],lines))

print(len(lines))

for line in lines:
    x1 = int(line[0][2:-1])
    y1 = int(line[1][2:-1])

    x2 = int(line[6][2:-1])
    y2 = int(line[7][2:])

    print(f"{x1} {y1} {x2} {y2}")

