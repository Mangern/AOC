import sys
with open(sys.argv[1], "r") as f:
    line = f.readlines()[0].strip()


i = 4
for sub in zip(line, line[1:], line[2:], line[3:]):
    s = set(sub)
    if len(s) == 4:
        print(i)
        break
    i += 1

