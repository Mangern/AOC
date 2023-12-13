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

    result = 0
    if num > i:
        # Result should stay 0 in this case
        pass
    elif s[i-1] == "#" and valid_place(s, a, i, j):
        result = combo(s, a, i - num - 1, j - 1)
    elif s[i-1] != "#":
        # Not place anything
        result += combo(s, a, i - 1, j)

        if valid_place(s, a, i, j):
            result += combo(s, a, i - num - 1, j - 1)

    return result

lines = open(sys.argv[1]).read().splitlines()

ans = 0
for line in lines:
    s, nums = line.split()
    nums = list(map(int, nums.split(",")))

    s = (s + "?")*4 + s
    nums = nums * 5

    memo = {}
    cnt = combo(s, nums, len(s), len(nums))

    ans += cnt

print(ans)

