def p2():
    with open("input.txt") as f:
        lines = f.readlines()

    trans = lambda line, i: line.split("|")[i].strip().split(" ")

    in_pairs = [(trans(line, 0), trans(line, 1)) for line in lines] 

    #   0
    # 1   2
    #   3
    # 4   5
    #   6

    def strsort(s):
        return "".join(sorted(s))

    def getmapping(strings):
        freq = {}

        for w in strings:
            for c in w:
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1

        mapping = {}

        for key in freq:
            if freq[key] == 6:
                mapping[key] = 1
            elif freq[key] == 4:
                mapping[key] = 4
            elif freq[key] == 9:
                mapping[key] = 5

        def assignmap(l, v):
            for w in strings:
                if len(w) == l:
                    for c in w:
                        if c not in mapping:
                            mapping[c] = v
                            return

        assignmap(2,2)
        assignmap(3,0)
        assignmap(4,3)
        assignmap(7,6)

        assert len(mapping) == 7
        return mapping


    def getd(mapping, string):
        digits = {
            (0,1,2,  4,5,6): "0",
            (    2,    5  ): "1",
            (0,  2,3,4,  6): "2",
            (0,  2,3,  5,6): "3",
            (  1,2,3,  5  ): "4",
            (0,1,  3,  5,6): "5",
            (0,1,  3,4,5,6): "6",
            (0,  2,    5  ): "7",
            (0,1,2,3,4,5,6): "8",
            (0,1,2,3,  5,6): "9"
        }

        return digits[tuple({mapping[c] for c in string})]


    def getnum(pair):
        mapping = getmapping(pair[0])

        return int("".join([getd(mapping, s) for s in pair[1]]))


    ans = sum([getnum(pair) for pair in in_pairs])
    print(ans)

p2()
