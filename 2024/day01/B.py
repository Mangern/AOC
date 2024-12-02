from sys import stdin
a, b = map(list, zip(*[map(int, line.split()) for line in stdin]))

bcnt = {}
for x in b:
    bcnt[x] = bcnt.get(x, 0) + 1

print(sum(x * bcnt.get(x, 0) for x in a))
