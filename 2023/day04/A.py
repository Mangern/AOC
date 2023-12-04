import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ans = 0
for i, line in enumerate(lines):
    lft, rgt = line.strip().split("|")
    lft = list(map(int, lft.split(":")[-1].split()))
    rgt = set(map(int, rgt.split()))
    
    mul = 1
    for x in rgt:
        if x in lft:
            mul <<= 1
    mul >>= 1
            
    ans += mul

print(ans)
