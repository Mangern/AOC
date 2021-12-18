with open("input.txt") as f:
    ans = 0
    nums = list(map(int, f.readlines()))

    ans = len(list(filter(lambda tup: tup[1] > tup[0], zip(nums, nums[1:]))))
    print(ans)

