from itertools import groupby

FILE_PREF = "input"

with open(f"{FILE_PREF}.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    scanner_lines = [list(line)[1:] for exclude, line in groupby(lines, lambda l: l == '') if not exclude]

with open(f"{FILE_PREF}.in", "w") as f:
    f.write(f"{len(scanner_lines)}\n")
    for scanner in scanner_lines:
        f.write(f"{len(scanner)}\n")
        for line in scanner:
            a,b,c = [int(x) for x in line.split(",")]
            f.write(f"{a} {b} {c}\n")
        f.write("\n")

