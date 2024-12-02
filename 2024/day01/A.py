from sys import stdin
a, b = map(list, zip(*[map(int, line.split()) for line in stdin]))

a.sort()
b.sort()

print(sum(abs(x-y) for x,y in zip(a,b)))
