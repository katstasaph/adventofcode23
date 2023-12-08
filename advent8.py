import re
from itertools import cycle
from math import lcm

with open("advent8.txt", "r") as f:
    path_data = f.read().splitlines()
    chosen_path = path_data[0]
    paths = {}
    for path in path_data[2:None]:
        data = re.findall(r'[A-Z]{3}', path)
        paths[data[0]] = [data[1], data[2]]
    current_point = "AAA"
    endpoint = "ZZZ"
    steps = 0
    # part 1
    for idx, dir in enumerate(cycle(chosen_path)):
        if (current_point == endpoint):
            break
        current_point = paths[current_point][0] if dir == "L" else paths[current_point][1]
        steps += 1
    print(f"part 1: {steps}")
    # part 2
    steps = []
    curr_points = [point for point in paths.keys() if point[2] == "A"]
    for point in curr_points:
        current_point = point
        curr_steps = 0
        for idx, dir in enumerate(cycle(chosen_path)):
            if current_point[2] == "Z":
                break
            current_point = paths[current_point][0] if dir == "L" else paths[current_point][1]
            curr_steps += 1
        steps.append(curr_steps)
    print(f"part 2: {lcm(*steps)}")

