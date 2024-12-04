from sys import stdin
import re

s = "".join(line for line in stdin)
t = s

pat = r"(?P<do>do\(\))|(?P<dont>don't\(\))|(?P<mul>mul\((?P<one>\d+),(?P<two>\d+)\))"
mtch = re.finditer(pat, t)

run = True
ans= 0

for x in mtch:
    if x.group("mul"):
        if run:
            a = int((x.group("one")))
            b = int((x.group("two")))
            ans += a * b
    elif x.group("do"):
        run = True
    elif x.group("dont"):
        run = False
print(ans)
