import sys
with open(sys.argv[1], "r") as f:
    lines = list(map(lambda s: s.strip(), f.readlines()))

lines = lines[1:]

curr_dir = "/" 

has = dict()
dirs = dict()
has["/"] = 0 
dirs["/"] = []

i = 0
while i < len(lines):
    line = lines[i]
    if line.find("$ cd") != -1:
        lst = line.split(" ")[-1]
        if lst == "/":
            curr_dir = "/"
        elif lst == "..":
            curr_dir = "/".join(curr_dir.split("/")[:-2]) + "/"
        else:
            curr_dir += lst + "/"
        i += 1
    else:
        i += 1
        while i < len(lines) and lines[i][0] != "$":
            lst = lines[i].split(" ")
            if lst[0] == "dir":
                if curr_dir not in dirs:
                    dirs[curr_dir] = []
                dirs[curr_dir].append(lst[1])
            else:
                x = int(lst[0])
                ptr = curr_dir
                while True:
                    if ptr not in has:
                        has[ptr] = 0
                    has[ptr] += x
                    if ptr == "/":
                        break
                    ptr = "/".join(ptr.split("/")[:-2]) + "/"
            i += 1

s = 0
for k in has:
    if has[k] <= 100000:
        s += has[k]
print(s)
