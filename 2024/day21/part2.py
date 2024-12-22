from sys import stdin
from part1 import Keypad, getlayout

DIR_PAD = Keypad(getlayout([" ^A", "<v>"]))

def search(s: str, level: int, dp: dict[tuple[str,int],int]) -> int:
    if level == 0:
        return len(s)

    key = (s, level)

    if key in dp:
        return dp[key]

    ways = DIR_PAD.dirs_code(s)
    dp[key] = 10**69
    for w in ways:
        parts = w.split('A')
        parts.pop()
        cost = sum(search(p + 'A', level - 1, dp) for p in parts)
        dp[key] = min(dp[key], cost)
    return dp[key]

if __name__ == "__main__":
    base = Keypad(getlayout(["789", "456", "123", " 0A"]))

    codes = [line.strip() for line in stdin]

    ans = 0
    dp = {}
    for code in codes:
        goals = base.dirs_code(code)

        best = float('inf')

        for goal in goals:
            parts = goal.split('A')
            parts.pop()
            cost = sum(search(p + 'A', 25, dp) for p in parts)
            best = min(best, cost)

        ans += best * int(code[:-1])


    print(ans)

