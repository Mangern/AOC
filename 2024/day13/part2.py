from sys import stdin

K = 10000000000000
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
    tx += K
    ty += K

    # s * xa + t * xb == tx
    # s * ya + t * yb == ty

    det = xa * yb - xb * ya

    if det != 0:
        i11 = yb
        i12 = -xb
        i21 = -ya
        i22 = xa

        # Ax = b
        # x = A^-1 b

        ibx = tx * i11 + ty * i12
        iby = tx * i21 + ty * i22
        if (ibx / det) >= 0 and ibx % det == 0 and (iby / det) >= 0 and iby % det == 0:
            s = ibx // det
            t = iby // det
            mini = 3 * s + t



    if mini != float('inf'):
        ans += mini

print(ans)
