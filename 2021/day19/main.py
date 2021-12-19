from itertools import groupby

def p1():
    with open("sample1_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        scanner_lines = [list(line) for exclude, line in groupby(lines, lambda l: l == '') if not exclude]


p1()