from itertools import pairwise

# part 1
def line_num_sum(line, line_idx, space_idx, seen):
    new_sum = 0
    for scan_idx in range(space_idx - 1, space_idx + 2):
        num = ""
        if (line[scan_idx].isdigit() and not seen.get(f"{line_idx},{scan_idx}")):
            # If we find a digit we haven't seen, scan left then right to capture the full number
            # We have to scan 2 characters in either direction since numbers can be up to 3 digits
            for idx in range(scan_idx - 2, scan_idx + 1):
                # edge case: "[end of unrelated number] . [start of number we're scanning]"
                if (idx == scan_idx - 2 and line[scan_idx - 1] == "."):
                    continue
                if (line[idx].isdigit() and not seen.get(f"{line_idx},{idx}")):
                    num = f"{num}{line[idx]}"
                    seen[f"{line_idx},{idx}"] = True
            for idx in range(scan_idx + 1, scan_idx + 3):
                if (not line[idx].isdigit()):
                    break
                num = f"{num}{line[idx]}"
                seen[f"{line_idx},{idx}"] = True
        new_sum += int(num or 0)
    return new_sum


def adjacent_num_sum(prev_line, curr_line, next_line, line_idx, space_idx, seen):
    new_sum = 0
    new_sum += line_num_sum(prev_line, line_idx - 1, space_idx, seen)
    new_sum += line_num_sum(curr_line, line_idx, space_idx, seen)
    new_sum += line_num_sum(next_line, line_idx + 1, space_idx, seen)
    return new_sum


# part 2

# Near-identical to above, but we push numbers to a list rather than summing as we go
def gear_nums(line, line_idx, space_idx, seen_gears):
    nums = []
    for scan_idx in range(space_idx - 1, space_idx + 2):
        num = ""
        if (line[scan_idx].isdigit() and not seen_gears.get(f"{line_idx},{scan_idx}")):
            for idx in range(scan_idx - 2, scan_idx + 1):
                if (idx == scan_idx - 2 and line[scan_idx - 1] == "."):
                    continue
                if (line[idx].isdigit() and not seen_gears.get(f"{line_idx},{idx}")):
                    num = f"{num}{line[idx]}"
                    seen_gears[f"{line_idx},{idx}"] = True
            for idx in range(scan_idx + 1, scan_idx + 3):
                if (not line[idx].isdigit()):
                    break
                num = f"{num}{line[idx]}"
                seen_gears[f"{line_idx},{idx}"] = True
        if (num != ""):
            nums.append(int(num))
    return nums


def adjacent_gear_sum(prev_line, curr_line, next_line, line_idx, space_idx, seen_gears):
    nums = []
    nums += gear_nums(prev_line, line_idx - 1, space_idx, seen_gears)
    nums += gear_nums(curr_line, line_idx, space_idx, seen_gears)
    if (len(nums) > 2): # If we already found 3+ numbers we don't have to do the last line check
        return 0
    nums += gear_nums(next_line, line_idx + 1, space_idx, seen_gears)
    if (len(nums) == 2):
        return nums[0] * nums[1]
    return 0


seen = {}
seen_gears = {}
sum = 0
gear_sum = 0
prev_line = ""

with open("advent3.txt", "r") as f:
    grid = f.read().splitlines()
    prev_line = ""
    for (line_idx, curr_line), (_, next_line) in pairwise(enumerate(grid)):
        for space_idx, space in enumerate(curr_line):
            if (space == "." or space.isdigit()):
                continue
            sum += adjacent_num_sum(prev_line, curr_line, next_line, line_idx, space_idx, seen)
            if (space == "*"):
                gear_sum += adjacent_gear_sum(prev_line, curr_line, next_line, line_idx, space_idx, seen_gears)
        prev_line = curr_line
    print("part 1:", sum)
    print("part 2:", gear_sum)
