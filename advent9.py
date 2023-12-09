from functools import reduce
from numpy import diff
import sympy

def finite_diffs(sequence):
    curr = [int(n) for n in sequence]
    diffs = [curr]
    while reduce(lambda a, b: a + b, curr) / len(curr) != curr[0]:
        curr = list(diff(curr))
        diffs.append(curr)
    return diffs

with open("advent9.txt", "r") as f:
    sequences = [line.split(" ") for line in f.read().splitlines()]
    sum = 0
    sum2 = 0
    for sequence in sequences:
        table = finite_diffs(sequence)[0]
        # If we can eventually derive common differences from a sequence, there exists some polynomial that produces it
        # more info:
        # www.cgsd.org/site/handlers/filedownload.ashx?moduleinstanceid=38&dataid=183&FileName=772-SMP-SEAA-C11L07.pdf
        poly = sympy.polys.specialpolys.interpolating_poly(len(table), sympy.symbols("x"),
                                                           [idx + 1 for (idx, _) in enumerate(table)], table)
        sum += poly.subs("x", (len(table)) + 1)
        sum2 += poly.subs("x", 0)
    print(f"part 1: {sum}")
    print(f"part 2: {sum2}")
