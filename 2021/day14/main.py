from functools import reduce
def p1():
    """ Dumb brute-force """
    with open("input.txt") as f:
        lines = f.readlines()

    template = list(lines[0][:-1])

    subst = {(s[0], s[1]): c.strip() for s,c in [line.split(" -> ") for line in lines[2:]]}

    def apply(template):
        subbed = [(el[0], subst[el], el[1]) if el in subst else (el[0], el[1]) for el in zip(template, template[1:])]

        res = list(subbed[0])

        for t in subbed[1:]:
            res += list(t[1:])

        return res

    for i in range(10):
        template = apply(template)

    def count_fun(cnts, char):
        if char in cnts:
            cnts[char] += 1
        else:
            cnts[char] = 1
        return cnts
    counts = reduce(count_fun, template, {})


    big,small = max({counts[c] for c in counts}), min({counts[c] for c in counts})
    print(big-small)


def p2():
    """ Big brain frequency analysis """
    with open("input.txt") as f:
        lines = f.readlines()

    template = list(lines[0][:-1])

    subst = {s: c.strip() for s,c in [line.split(" -> ") for line in lines[2:]]}

    def count(lst):
        """ Makes a map from every element to its count in lst """
        res = dict()

        for el in lst:
            if el in res:
                res[el] += 1
            else:
                res[el] = 1
        return res

    freq = count(["".join(l) for l in zip(template, template[1:])])

    dicsub = {app[0] + app[2]: count([p[0] + p[1] for p in zip(app, app[1:])]) 
                                for app in [s[0] + subst[s] + s[1] for s in subst]}

    def apply(freqs):
        new_freqs = dict()

        for key in freqs:
            num = freqs[key]

            res = dicsub[key]

            for k in res:
                if k in new_freqs:
                    new_freqs[k] += num
                else:
                    new_freqs[k] = num

        return new_freqs

    for i in range(40):
        freq = apply(freq)

    charcnt = dict()

    for key in freq:
        c = key[0]
        if c in charcnt:
            charcnt[c] += freq[key]
        else:
            charcnt[c] = freq[key]

    charcnt[template[-1]] += 1

    big,small = max({charcnt[k] for k in charcnt}), min({charcnt[k] for k in charcnt})

    print(big-small)

p2()
