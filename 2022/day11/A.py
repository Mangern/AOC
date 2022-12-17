import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: l.split(), f.readlines()))

n = ((len(lines)+1)//7)
print(n)

j = 0
for i in range(n):
    j += 1
    to_pr = " ".join(map(lambda s: s if s[-1] != "," else s[:-1], lines[j][2:]))
    print(len(to_pr.split(" ")))
    print(to_pr)
    j += 1
    print(lines[j][-2] + " " + lines[j][-1])
    j += 1
    print(lines[j][-1])
    j += 1
    print(lines[j][-1])
    j += 1
    print(lines[j][-1])
    j += 2
