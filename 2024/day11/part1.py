def mp(x):
    if x == 0:
        return [1]
    s = str(x)
    if len(s) % 2 == 0:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    return [2024 * x]

def ev(a):
    b = []
    for x in a:
        for y in mp(x):
            b.append(y)
    return b

if __name__ == "__main__":
    s = list(map(int, input().split()))

    for _ in range(25):
        s = ev(s)

    print(len(s))
