import sys
with open(sys.argv[1], "r") as f:
    line = f.readlines()[0].strip()


i = 14
for sub in zip(line, line[1:], line[2:], line[3:], line[4:], line[5:], line[6:], line[7:], line[8:], line[9:], line[10:], line[11:], line[12:], line[13:]):
    s = set(sub)
    if len(s) == 14:
        print(i)
        break
    i += 1

