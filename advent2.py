import re

CUBES = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def valid_game(set):
    red = re.search(r'\d+(?= red)', set)
    green = re.search(r'\d+(?= green)', set)
    blue = re.search(r'\d+(?= blue)', set)
    return ((not red or int(red.group(0)) <= CUBES["red"])
            and (not green or int(green.group(0)) <= CUBES["green"])
            and (not blue or int(blue.group(0)) <= CUBES["blue"])
    )

# part 1

f = open("advent2.txt", "r")
games = f.read().splitlines()
sum = 0
for game in games:
  valid = True
  id = re.search(r'\d+(?=:)', game).group(0)
  cube_sets = game.split(": ")[1].split(";")
  for set in cube_sets:
      if (not valid_game(set)):
          valid = False
          break
  if (valid):
      sum += int(id)
print(sum)

# part 2

def minimum_power(set):
    red_matches = re.findall(r'\d+(?= red)', set)
    green_matches = re.findall(r'\d+(?= green)', set)
    blue_matches = re.findall(r'\d+(?= blue)', set)
    red_totals = [int(n) for n in red_matches]
    green_totals = [int(n) for n in green_matches]
    blue_totals = [int(n) for n in blue_matches]
    return max(red_totals, default=1) * max(green_totals, default=1) * max(blue_totals, default=1)

power_sum = 0
for game in games:
    id = re.search(r'\d+(?=:)', game).group(0)
    power_sum += minimum_power(game)
print(power_sum)
f.close()