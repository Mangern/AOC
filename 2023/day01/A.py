import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

digis = [
    [c for c in line if ord(c) in range(ord('0'), ord('9')+1)]

for line in lines]

print(sum(int(dig[0]+dig[-1]) for dig in digis))
