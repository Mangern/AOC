from copy import deepcopy
def p1():
    with open("input.txt") as f:
        fish_nums = [eval(line.strip()) for line in f.readlines()]

    def add(a, b):
        return [a,b]

    def is_base_pair(x):
        return isinstance(x, list) and len(x) == 2 and isinstance(x[0], int) and isinstance(x[1], int)

    def find_explode(a, path = []):
        """
        Path: 0 = left, 1 = right 
        Return: Bool, path?
        """

        if len(path) == 4 and is_base_pair(a):
            return True, path

        if isinstance(a, int):
            return False, [] 

        res_left, path_left = find_explode(a[0], path + [0])
        if res_left:
            return True, path_left

        res_right, path_right = find_explode(a[1], path + [1]) 
        if res_right:
            return True, path_right

        return False, path

    def explode(a):
        res, path = find_explode(a)

        if not res:
            return False

        it = a

        for i in path:
            it = it[i]

        lft,rgt = it

        it = a

        last_right = None
        last_left = None

        for i in path[:-1]:
            it = it[i]

        # reset to 0
        it[path[-1]] = 0

        it = a
        for i in path:
            if i == 0:
                last_left = it
            else:
                last_right = it
            it = it[i]

        if last_right is not None:
            ptr = 0
            while not isinstance(last_right[ptr], int):
                last_right = last_right[ptr]

                if ptr == 0:
                    ptr = 1

            last_right[ptr] += lft

        if last_left is not None:
            ptr = 1
            while not isinstance(last_left[ptr], int):
                last_left = last_left[ptr]

                if ptr == 1:
                    ptr = 0

            last_left[ptr] += rgt

        return True

    def split(a):
        """
        Returns true if split was performed
        """

        if isinstance(a, int):
            return False

        if isinstance(a[0], int):
            if a[0] >= 10:
                num = a[0]
                a[0] = [num>>1, (num+1)>>1]
                return True

        elif split(a[0]):
            return True

        if isinstance(a[1], int):
            if a[1] >= 10:
                num = a[1]
                a[1] = [num>>1, (num+1)>>1]
                return True
        
        return split(a[1])

    def reduce(a):
        """ 
        Reduces as much as possible
        Modifies a
        """
        while True:
            if explode(a):
                continue
            if split(a):
                continue
            break

    def mag(a):
        if isinstance(a, int):
            return a

        return 3 * mag(a[0]) + 2 * mag(a[1])

    result = fish_nums[0]

    for num in fish_nums[1:]:
        result = add(result, num)
        reduce(result)

    print(mag(result))

def p2():
    with open("input.txt") as f:
        fish_nums = [eval(line.strip()) for line in f.readlines()]


    def is_base_pair(x):
        return isinstance(x, list) and len(x) == 2 and isinstance(x[0], int) and isinstance(x[1], int)

    def find_explode(a, path = []):
        """
        Path: 0 = left, 1 = right 
        Return: Bool, path?
        """

        if len(path) == 4 and is_base_pair(a):
            return True, path

        if isinstance(a, int):
            return False, [] 

        res_left, path_left = find_explode(a[0], path + [0])
        if res_left:
            return True, path_left

        res_right, path_right = find_explode(a[1], path + [1]) 
        if res_right:
            return True, path_right

        return False, path

    def explode(a):
        res, path = find_explode(a)

        if not res:
            return False

        it = a

        for i in path:
            it = it[i]

        lft,rgt = it

        it = a

        last_right = None
        last_left = None

        for i in path[:-1]:
            it = it[i]

        # reset to 0
        it[path[-1]] = 0

        it = a
        for i in path:
            if i == 0:
                last_left = it
            else:
                last_right = it
            it = it[i]

        if last_right is not None:
            ptr = 0
            while not isinstance(last_right[ptr], int):
                last_right = last_right[ptr]

                if ptr == 0:
                    ptr = 1

            last_right[ptr] += lft

        if last_left is not None:
            ptr = 1
            while not isinstance(last_left[ptr], int):
                last_left = last_left[ptr]

                if ptr == 1:
                    ptr = 0

            last_left[ptr] += rgt

        return True

    def split(a):
        """
        Returns true if split was performed
        """

        if isinstance(a, int):
            return False

        if isinstance(a[0], int):
            if a[0] >= 10:
                num = a[0]
                a[0] = [num>>1, (num+1)>>1]
                return True

        elif split(a[0]):
            return True

        if isinstance(a[1], int):
            if a[1] >= 10:
                num = a[1]
                a[1] = [num>>1, (num+1)>>1]
                return True
        
        return split(a[1])

    def reduce(a):
        """ 
        Reduces as much as possible
        Modifies a
        """
        while True:
            if explode(a):
                continue
            if split(a):
                continue
            break

    def mag(a):
        if isinstance(a, int):
            return a

        return 3 * mag(a[0]) + 2 * mag(a[1])

    def add(a, b):
        result = [a,b]
        reduce(result)
        return result 


    ans = 0

    for i,a in enumerate(fish_nums):
        for j,b in enumerate(fish_nums):
            if i == j:
                continue
            ans = max(ans, mag(add(deepcopy(a),deepcopy(b))), mag(add(deepcopy(b),deepcopy(a))))

    print(ans)

p2()
