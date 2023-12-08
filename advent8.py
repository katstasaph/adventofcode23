import re
from itertools import cycle
from math import lcm


def pathfind(paths, endpoint, dp, path_str):
    prev_points = [key for key in paths if (paths[key][0] == endpoint) or (paths[key][1] == endpoint)]
    if (not len(prev_points) or len(dp.keys()) >= len(paths.keys())):
        return
    for point in prev_points:
        if (not dp.get(point)):
            dp[point] = []
        elif (len(dp[point])):
            continue
        if (paths[point][0] == endpoint):
            dp[point].append("L" + path_str)
        if (paths[point][1] == endpoint):
            dp[point].append("R" + path_str)
        for str in dp[point]:
            pathfind(paths, point, dp, str)


def pathfind_part_2(paths, end, dp, path_str):
    prev_points = [key for key in paths if (paths[key][0][2] == end) or (paths[key][1][2] == end)]
    print(prev_points)
    if (not len(prev_points) or len(dp.keys()) >= len(paths.keys())):
        return
    for point in prev_points:
        if (not dp.get(point)):
            dp[point] = []
        elif (len(dp[point])):
            continue
        if (paths[point][0] == endpoint):
            dp[point].append("L" + path_str)
        if (paths[point][1] == endpoint):
            dp[point].append("R" + path_str)
        for str in dp[point]:
            pathfind(paths, point, dp, str)


def done(current_point, endpoint, chosen_path, idx, dp):
    return current_point == endpoint or \
           (dp.get(current_point) and chosen_path[idx:None].startswith(dp[current_point][0]))


def done_part_2(current_point, chosen_path, idx, dp):
    return current_point[2] == "Z" or \
           (dp.get(current_point) and chosen_path[idx:None].startswith(dp[current_point][0]))


with open("advent8.txt", "r") as f:
    path_data = f.read().splitlines()
    chosen_path = path_data[0]
    paths = {}
    for path in path_data[2:None]:
        data = re.findall(r'[A-Z]{3}', path)
        paths[data[0]] = [data[1], data[2]]
    dp = {}
    current_point = "AAA"
    endpoint = "ZZZ"
    pathfind(paths, endpoint, dp, "")
    steps = 0
    # part 1
    for idx, dir in enumerate(cycle(chosen_path)):
        if (done(current_point, endpoint, chosen_path, idx, dp)):
            break
        current_point = paths[current_point][0] if dir == "L" else paths[current_point][1]
        steps += 1
    print(f"part 1: {steps}")
    # part 2
    steps = []
    dp = {}
    curr_points = [point for point in paths.keys() if point[2] == "A"]
    end_points = [point for point in paths.keys() if point[2] == "Z"]
    for end in end_points:
        pathfind(paths, end, dp, "")
    for point in curr_points:
        current_point = point
        curr_steps = 0
        for idx, dir in enumerate(cycle(chosen_path)):
            if (done_part_2(current_point, chosen_path, idx, dp)):
                break
            current_point = paths[current_point][0] if dir == "L" else paths[current_point][1]
            curr_steps += 1
        steps.append(curr_steps)
    print(f"part 2: {lcm(*steps)}")
