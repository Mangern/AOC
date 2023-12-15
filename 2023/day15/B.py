import sys

def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

boxes = [[] for _ in range(256)]

for op in open(sys.argv[1]).read().strip().split(","):
    if "=" in op:
        name, val = op.split("=")
        val = int(val)
        idx = hash(name)

        for i, (nm, v) in enumerate(boxes[idx]):
            if nm == name:
                boxes[idx][i][1] = val
                break
        else:
            boxes[idx].append([name, val])

    elif op[-1] == "-":
        name = op[:-1]
        idx = hash(name)
        boxes[idx] = [[n, v] for n, v in boxes[idx] if n != name]
    else:
        assert False, "Unknown OP"

ans = 0
for bid, lst in enumerate(boxes):
    for i, (_, val) in enumerate(lst):
        ans += (bid + 1) * (i + 1) * val
print(ans)
