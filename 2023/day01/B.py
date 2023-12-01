import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ws = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


digis = []

for line in lines:
    digis.append([])
    for i, c in enumerate(line):
        if ord(c) in range(ord('0'), ord('9')+1):
            digis[-1].append(c)
        for j, w in enumerate(ws):
            if line[i:i+len(w)] == w:
                digis[-1].append(str(j+1))


print(sum(int(dig[0]+dig[-1]) for dig in digis))

