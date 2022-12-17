import sys
import json
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



i = 1
ans = 0
for list1, list2 in zip(lines[::2], lines[1::2]):
    if comp(list1,list2) == 1:
        ans += i
    i += 1

print(ans)
