with open("input.txt") as f:
    lines = f.readlines()

    pairs = [line.split("->") for line in lines]

    print(len(lines))
    for p in pairs:
        a, b = p[0].strip().split(",")
        c, d = p[1].strip().split(",")

        print(f"{a} {b} {c} {d}")
