from sys import stdin
import re

s = "".join(line for line in stdin)
t = s

pat = r"mul\((\d+),(\d+)\)"
mtch = re.findall(pat, t)

ans = 0
for a,b in mtch:
    ans += int(a)*int(b)
print(ans)
