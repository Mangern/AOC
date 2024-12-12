from part1 import mp

def ev(a):
    b = {}
    for x in a:
        for y in mp(x):
            b[y] = b.get(y, 0) + a[x]
    return b

if __name__ == "__main__":
    s = list(map(int, input().split()))
    d = {}
    for x in s:
        d[x] = d.get(x, 0) + 1

    for _ in range(75):
        d = ev(d)

    print(sum(d.values()))
