import sys

def valid_place(s, a, i, j):
    num = a[j-1]
    if num < i and s[i-num-1] == '#':
        return False

    if "." in s[i-num:i]:
        return False

    return True

def combo(s, a, i, j):
    if j == 0:
        if i >= 0 and "#" in s[:i]:
            return 0
        return 1
    if i <= 0:
        return 0

    num = a[j-1]
    if num > i:
        return 0

    #    12345678
    #    ??...?##
    #          l i

    if s[i-1] == "#":
        if valid_place(s, a, i, j):
            result = combo(s, a, i - num - 1, j - 1)
        else:
            return 0
    else:
        # Not place anything
        result = combo(s, a, i - 1, j)

        if valid_place(s, a, i, j):
            result += combo(s, a, i - num - 1, j - 1)
    return result

lines = open(sys.argv[1]).read().splitlines()

ans = 0
for line in lines:
    s, nums = line.split()
    nums = list(map(int, nums.split(",")))
    cnt = combo(s, nums, len(s), len(nums))
    ans += cnt
    print(s, nums, cnt)

print(ans)
