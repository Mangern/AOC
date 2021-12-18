with open("input.txt") as f: (lambda nums: print(len(list(filter(lambda tup: tup[1] > tup[0], zip(nums, nums[3:]))))))(list(map(int,f.readlines())))
