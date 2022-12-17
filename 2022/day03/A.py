import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

sm = 0
for line in lines:
    lft = set()
    rgt = set()
    for i,c in enumerate(line):
        if i < len(line)//2:
            lft.add(c)
        else:
            rgt.add(c)
    el = (lft.intersection(rgt)).pop()
    if ord("A") <= ord(el) <= ord("Z"):
        sm += ord(el) - ord("A")+27
    else:
        sm += ord(el) - ord("a")+1

print(sm)
