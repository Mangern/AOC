from functools import reduce
import sys

print(
    sum(
        map(lambda s: 
            reduce(
                lambda res, c: 
                    17 * (res + ord(c)) % 256,
                s,
                0
            ), 
            open(sys.argv[1])
                .read()
                .strip()
                .split(",")
        )
))
