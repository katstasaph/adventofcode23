from re import findall
from functools import reduce
from numpy import roots

def ways_to_win(race):
    constant = int(race[0])
    for x in range(0, constant):
        y = (constant * x) - (x*x)
        if (y > int(race[1])):
            bounds = roots([1, -constant, y])
            return int(abs(bounds[0] - bounds[1]) + 1)
    return 0

with open("advent6.txt", "r") as f:
    race_data = f.read().splitlines()
    times = [int(n) for n in findall(r'\d+', race_data[0])]
    recs = [int(n) for n in findall(r'\d+', race_data[1])]
    races = zip(times, recs)
    big_race = [(reduce(lambda n1, n2: str(n1) + str(n2), times)),
                (reduce(lambda n1, n2: str(n1) + str(n2), recs))]
    multiplied = 0
    for race in races:
        ways = ways_to_win(race)
        multiplied = multiplied * ways if multiplied else ways
    print(f"part 1: {multiplied}")
    print(f"part 2: {ways_to_win(big_race)}")
