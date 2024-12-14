from sys import stdin

arr = []

tp = []
for line in stdin:
    s = line.strip()
    if not s:
        continue

    if s.startswith("Button"):
        s = s[10:]
        a, b = s.split(", ")
        x = int(a[2:])
        y = int(b[2:])
        tp.append((x,y))
    else:
        s = s[7:]
        a, b = s.split(", ")
        x = int(a[2:])
        y = int(b[2:])
        tp.append((x,y))
        arr.append(tp)
        tp = []

ans = 0

for (xa, ya), (xb, yb), (tx, ty) in arr:
    mini = float('inf')
    for i in range(100):
        rx = tx - i * xa
        ry = ty - i * ya
        if rx < 0 or ry < 0:
            continue
        if rx % xb != 0:
            continue
        if ry % yb != 0:
            continue
        if rx // xb != ry // yb:
            continue
        mini = min(mini, 3 * i + rx // xb)
    if mini == float('inf'):
        continue
    ans += mini

print(ans)
