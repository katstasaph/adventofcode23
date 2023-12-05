from re import findall
from operator import itemgetter
from itertools import islice, batched
from math import inf


# code not guaranteed pythonic

def convert(stage, step):
    for entry in step:
        if (stage >= int(entry[1]) and stage < int(entry[1]) + int(entry[2])):
            stage += int(entry[0]) - int(entry[1])
            break
    return stage


def find_lowest(seeds, steps):
    lowest = inf
    for seed in seeds:
        stage = seed
        for step in steps:
            stage = convert(stage, step)
        lowest = stage if stage < lowest else lowest
    return lowest


def parse(data):
    soil = [findall(r'\d+', entry) for entry in islice(data, 2, data.index("soil-to-fertilizer map:"))]
    fertilizer = [findall(r'\d+', entry) for entry in
                  islice(data, data.index("soil-to-fertilizer map:") + 1, data.index("fertilizer-to-water map:"))]
    water = [findall(r'\d+', entry) for entry in
             islice(data, data.index("fertilizer-to-water map:") + 1, data.index("water-to-light map:"))]
    light = [findall(r'\d+', entry) for entry in
             islice(data, data.index("water-to-light map:") + 1, data.index("light-to-temperature map:"))]
    temp = [findall(r'\d+', entry) for entry in
            islice(data, data.index("light-to-temperature map:") + 1, data.index("temperature-to-humidity map:"))]
    humidity = [findall(r'\d+', entry) for entry in
                islice(data, data.index("temperature-to-humidity map:") + 1, data.index("humidity-to-location map:"))]
    location = [findall(r'\d+', entry) for entry in
                islice(data, data.index("humidity-to-location map:") + 1, len(data))]
    return [soil, fertilizer, water, light, temp, humidity, location]


# Part 2 only

def seeds_to_ranges(seeds):
    ranges = [list(n) for n in batched(seeds, 2)]
    sorted_ranges = [[pair[0], pair[0] + pair[1] - 1] for pair in ranges]
    # Merge intervals to remove redundancies
    return merge(sorted_ranges)


# leetcode time
def merge(intervals):
    intervals = sorted(intervals, key=itemgetter(0))
    compressed = [intervals[0]]
    for interval in intervals:
        if (interval[0] <= compressed[-1][1]):
            compressed[-1][1] = max(interval[1], compressed[-1][1])
        else:
            compressed.append(interval)
    return compressed


def usable_ranges(ranges, step):
    # Get our ranges back into merged sorted form
    ranges = merge(ranges)
    usable = []
    # The greatest number any rule covers; once we reach it we're done splitting ranges
    last_cutoff = int(step[-1][1]) + int(step[-1][2])
    for seed_range in ranges:
        curr_range = seed_range.copy()
        if (curr_range[0] > last_cutoff):
            # Add any remaining ranges to our list
            for range in ranges:
                if (range[0] > usable[-1][1]):
                    usable.append(range)
            return usable
        for entry in step:
            # Current range is entirely greater than the current entry
            if (curr_range[0] > int(entry[1]) + int(entry[2]) - 1):
                continue
            # Current range falls entirely within current entry
            if (curr_range[1] <= int(entry[1]) + int(entry[2]) - 1):
                usable.append(curr_range)
                break
            # Current range extends beyond current entry, must be split
            else:
                new_range = curr_range.copy()
                new_range[1] = int(entry[1]) + int(entry[2]) - 1
                usable.append(new_range)
                curr_range = curr_range.copy()
                curr_range[0] = int(entry[1]) + int(entry[2])
                continue


def convert_with_range(seed_range, step):
    converted = []
    for entry in step:
        if (seed_range[0] < int(entry[1])):
            continue
        elif (seed_range[0] <= int(entry[1]) + int(entry[2]) - 1):
            converted.append(seed_range[0] + int(entry[0]) - int(entry[1]))
            converted.append(seed_range[1] + int(entry[0]) - int(entry[1]))
            break
    return converted if len(converted) else seed_range


def find_lowest_with_range(ranges, steps):
    curr_ranges = ranges
    converted = []
    for step in steps:
        new_ranges = usable_ranges(curr_ranges, step)
        converted = [convert_with_range(seed_range, step) for seed_range in new_ranges]
        curr_ranges = converted
    return converted[0][0]


with open("advent5.txt", "r") as f:
    data = [line for line in f.read().splitlines() if line != '\n' and line != '']
    seeds = [int(n) for n in findall(r'\d+', data[0])]
    ranges = seeds_to_ranges(seeds)
    steps = parse(data)
    sorted_steps = [sorted(step, key=itemgetter(1)) for step in steps]
    print(f"part 1: {find_lowest(seeds, steps)}")
    print(f"part 2: {find_lowest_with_range(ranges, sorted_steps)}")
