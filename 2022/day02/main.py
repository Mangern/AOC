with open("input", "r") as f:
    lines = f.readlines()


beats = {
        "A": "B",
        "B": "C",
        "C": "A"
}

beated = {
        "A": "C",
        "B": "A",
        "C": "B"
}

score = {
        "A": 1,
        "B": 2,
        "C": 3
}

sm = 0
for line in lines:
    if not len(line.strip()):
        continue
    chars = line.strip().split()

    fst = chars[0]
    ch = chars[1]

    if ch == "X":
        scn = beated[fst]
    elif ch == "Y":
        scn = fst
    else:
        scn = beats[fst]

    if beats[fst] == scn:
        sm += 6
    elif fst == scn:
        sm += 3
    sm += score[scn]

print(sm)
