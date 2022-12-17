import sys
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

stacks = []

k = 0
for line in lines:
    if line[1] == "1":
        k += 2
        break
    i = 1
    j = 0
    while i < len(line):
        if len(stacks)==j:
            stacks.append([])
        if ord("A") <= ord(line[i]) <= ord("Z"):
            stacks[j].append(line[i])
        i += 4
        j += 1
    k += 1

stacks = list(map(lambda s: list(reversed(s)), stacks))

print(stacks)

for line in lines[k:]:
    cmds = list(map(lambda c: int(c)-1, line.strip().split(" ")[1::2]))

    curr = []
    j = cmds[2]
    for p in range(cmds[0]+1):
        i = cmds[1]
        x = stacks[i].pop()
        curr.append(x)
    while len(curr):
        stacks[j].append(curr.pop())

print("".join(map(lambda s: s[-1],stacks)))
