import re
from functools import reduce

with open("advent4.txt", "r") as f:
    total = 0
    lines = f.read().splitlines()
    new_card_totals = {(id): 1 for (id, _) in enumerate(lines)}
    for card_id, card in enumerate([line.split(": ")[1] for line in lines]):
        winning_numbers = {}
        winners = 0
        card_score = 0
        for num_id, num in enumerate(re.findall(r'\d+', card)):
            if (num_id < 10):
                winning_numbers[num] = True
            elif (winning_numbers.get(num)):
                winners += 1
        for bonus_id in range(1, winners + 1):
            new_card_totals[bonus_id + card_id] += new_card_totals[card_id]
        card_score = pow(2, (winners - 1)) if winners > 0 else 0
        total += card_score
    print(f"part 1: {total}")
    print(f"part 2: {reduce(lambda a, b: a + b, new_card_totals.values())}")
