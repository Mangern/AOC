from sys import stdin
from itertools import permutations, product
KeypadLayout = dict[str, tuple[int,int]]

class Keypad:
    def __init__(self, layout: KeypadLayout):
        self.layout = layout

    def dirs_char(self, start: tuple[int,int], goal: tuple[int,int]) -> list[str]:
        def tochar(delta: tuple[int,int]) -> str:
            return {
                (-1,  0): "^",
                ( 1,  0): "v",
                ( 0, -1): "<",
                ( 0,  1): ">"
            }[delta]
        di = 1 if goal[0] > start[0] else -1
        dj = 1 if goal[1] > start[1] else -1
        seq = [(di, 0)] * abs(goal[0] - start[0]) + [(0, dj)] * abs(goal[1] - start[1])

        ret = []
        for p in permutations(seq):
            pos = start
            bad = False
            for delta in p:
                if pos == self.layout[' ']:
                    bad = True
                    break
                pos = (pos[0] + delta[0], pos[1] + delta[1])
            if bad:
                continue
            ret.append("".join(map(tochar, p)))
        return ret


    def dirs_code(self, code: str) -> set[str]:
        pos = self.layout['A']
        res = {""}
        for c in code:
            nxt = self.layout[c]
            ret = [s + 'A' for s in self.dirs_char(pos, nxt)]
            res = list(set("".join(seq) for seq in product(res, ret)))
            pos = nxt
        slen = min(map(len, res))
        res = {s for s in res if len(s) == slen}
        return res


def getlayout(grid: list[str]) -> KeypadLayout:
    layout = {}

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            layout[c] = (i, j)

    return layout

if __name__ == "__main__":
    chain = [
        Keypad(getlayout(["789", "456", "123", " 0A"])),
        Keypad(getlayout([" ^A", "<v>"])),
        Keypad(getlayout([" ^A", "<v>"])),
    ]

    codes = [line.strip() for line in stdin]

    ans = 0
    for code in codes:
        cur = [code]

        for pad in chain:
            pool: set[str] = set()
            for c in cur:
                pool |= pad.dirs_code(c)
            slen = min(map(len, pool))
            cur = {s for s in pool if len(s) == slen}

        l = len(cur.pop())
        v = int(code[:-1])
        ans += l * v
        print(len(cur))
    print(ans)

