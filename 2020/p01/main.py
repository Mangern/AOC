def main1():
    with open("input.txt") as f:
        nums = list(map(int, f.readlines()))

        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if a + b == 2020:
                    print(a*b)

def main2():
    with open("input.txt") as f:
        nums = list(map(int, f.readlines()))

        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                for k, c in enumerate(nums):
                    if a + b + c == 2020:
                        print(a*b*c)

main2()
