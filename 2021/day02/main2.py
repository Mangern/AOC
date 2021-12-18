# 1281977850
with open("input.txt") as f:
    x_pos = 0
    y_pos = 0
    aim = 0

    lines = f.readlines()

    for line in lines:
        s, x = line.split(" ")
        x = int(x)

        if s == "down":
            aim += x
        elif s == "up":
            aim -= x
        elif s == "forward":
            x_pos += x
            y_pos += aim * x

    print(x_pos*y_pos)
