import sys
rang = lambda s: tuple(map(int, s.split("-")))
with open(sys.argv[1], "r") as f:
    ranges = list(map(lambda line: tuple(map(rang,line.split(","))), f.readlines()))
ans = 0
for a,b in ranges:
    if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]):
        a,b = b,a
    if a[1] >= b[0]:
        ans += 1
print(ans)
