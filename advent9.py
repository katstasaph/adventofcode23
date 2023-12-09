import sympy

with open("advent9.txt", "r") as f:
    sequences = [line.split(" ") for line in f.read().splitlines()]
    sum = 0
    sum2 = 0
    for sequence in sequences:
        nums = [int(n) for n in sequence]
        # If we can eventually derive common differences from a sequence, there exists some polynomial that produces it
        # more info:
        # www.cgsd.org/site/handlers/filedownload.ashx?moduleinstanceid=38&dataid=183&FileName=772-SMP-SEAA-C11L07.pdf
        poly = sympy.polys.specialpolys.interpolating_poly(len(nums), sympy.symbols("x"),
                                                           [idx + 1 for (idx, _) in enumerate(nums)], nums)
        sum += poly.subs("x", (len(nums)) + 1)
        sum2 += poly.subs("x", 0)
    print(f"part 1: {sum}")
    print(f"part 2: {sum2}")
