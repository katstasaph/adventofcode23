from re import findall
from functools import reduce
from math import ceil, floor
from numpy import roots


def ways_to_win(race):
    constant = int(race[0])
    bounds = sorted(roots([1, -constant, int(race[1])]))
    if (bounds[1].is_integer()):
        return int(bounds[1]) - 2 - int(bounds[0]) + 1
    else:
        return int((ceil(bounds[1]) - 2 - floor(bounds[0]))) + 1


with open("advent6.txt", "r") as f:
    race_data = f.read().splitlines()
    times = findall(r'\d+', race_data[0])
    recs = findall(r'\d+', race_data[1])
    races = zip(times, recs)
    big_race = [reduce(lambda n1, n2: n1 + n2, times),
                reduce(lambda n1, n2: n1 + n2, recs)]
    multiplied = 0
    for race in races:
        ways = ways_to_win(race)
        multiplied = multiplied * ways if multiplied else ways
    print(f"part 1: {multiplied}")
    print(f"part 2: {ways_to_win(big_race)}")
