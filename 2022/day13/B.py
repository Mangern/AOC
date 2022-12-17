import sys
import json
from functools import cmp_to_key
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda l: json.loads(l.strip()) if l != "\n" else "", f.readlines()))

lines = list(filter(lambda x: x != "", lines))

def comp(list1, list2):
    if type(list1) == list and type(list2) == list:
        for i in range(min(len(list1), len(list2))):
            ret = comp(list1[i], list2[i])
            if ret != 0:
                return ret
        if len(list1) == len(list2):
            return 0
        if len(list1) < len(list2):
            return 1
        return -1
    elif type(list1) == list:
        return comp(list1, [list2])
    elif type(list2) == list:
        return comp([list1], list2)
    else:
        if list1 < list2:
            return 1
        if list1 > list2:
            return -1
        return 0



lines.append([[6]])
lines.append([[2]])

lines = reversed(sorted(lines, key=cmp_to_key(comp)))

a1 = 0
a2 = 0
for i,l in enumerate(lines):
    if l == [[2]]:
        a1 = i+1
    elif l == [[6]]:
        a2 = i+1

print(a1 * a2)


