import sys

def card_type(s):
    s = "".join(sorted(s))
    if "J" in s:
        return brute(s)
    if s == s[0]*5:
        # Five of a kind
        return 6
    if s == s[0]*4 + s[-1] or s == s[0] + s[1]*4:
        # Four of a kind
        return 5
    if s == s[0]*2 + s[2]*3 or  s == s[0]*3 + s[3]*2:
        # Full house
        return 4
    if s == s[0] + s[1]*3 + s[-1] or s == s[0]*3 + s[-2] + s[-1] or s == s[0] + s[1] + s[2]*3:
        # Three of a kind
        return 3
    if len(set(s)) == 3:
        # Two pairs
        return 2
    if len(set(s)) == 4:
        # One pair
        return 1
    return 0

def brute(s):
    refs = "23456789TQKA"
    i = s.index("J")
    s = list(s)
    ret = 0
    for c in refs:
        s[i] = c
        ret = max(ret, card_type("".join(s)))
    return ret

def value(s):
    refs = "J23456789TQKA"
    return tuple(refs.index(c) for c in s)

with open(sys.argv[1]) as f:
    lines = f.readlines()

cards = []
for line in lines:
    card, bid = line.split()
    cards.append((
        card_type(card),
        value(card),
        int(bid)
    ))

print(sum((i+1) * z for i, (_, _, z) in enumerate(sorted(cards))))

