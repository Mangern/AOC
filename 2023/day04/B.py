import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ans = 0
n = len(lines)

cnt = [1] * n

for i, line in enumerate(lines):
    lft, rgt = line.strip().split("|")
    lft = list(map(int, lft.split(":")[-1].split()))
    rgt = set(map(int, rgt.split()))
    
    j = 1
    for x in rgt:
        if x in lft and i + j < n:
            cnt[i+j] += cnt[i]
            j += 1



print(sum(cnt))
