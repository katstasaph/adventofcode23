def find_hand_type(hand, totals, jokers=False):
    matches = 0
    two_pair = False
    full_house = False
    for card in hand[0]:
        totals[card] = totals[card] + 1 if totals.get(card) else 1
        if (jokers and card == "1"):
            continue
        if (matches == 2 and totals[card] == 2):
            two_pair = True
        if (totals[card] > matches):
            matches += 1
        if (matches == 3 and (two_pair or totals[card] == 2)):
            full_house = True
    if (jokers):
        return adjusted_joker_data(totals, matches, two_pair, full_house)
    return (matches, two_pair, full_house)

def adjusted_joker_data(totals, matches, two_pair, full_house):
    if (not totals.get("1")):
        return (matches, two_pair, full_house)
    elif (totals["1"] >= 4):
        return (5, two_pair, False)
    elif (totals["1"] == 3):
        if (matches == 2):
            return (5, two_pair, False)
        else:
            return (4, two_pair, False)
    elif (totals["1"] == 2):
        return (matches + 2, two_pair, False)
    elif (totals["1"] == 1):
        if (two_pair):
            return (3, two_pair, True)
        else:
            return (matches + 1, two_pair, False)

def sort_hands(categories):
    for category in categories:
        category.sort(key = lambda a: a[0])

def categorize(hand, hand_data, hand_categories):
    if (hand_data[0] == 5):
        hand_categories[6].append(hand)
    elif (hand_data[0] == 4):
        hand_categories[5].append(hand)
    elif (hand_data[2]):
        hand_categories[4].append(hand)
    elif (hand_data[0] == 3):
        hand_categories[3].append(hand)
    elif (hand_data[1]):
        hand_categories[2].append(hand)
    elif (hand_data[0] == 2):
        hand_categories[1].append(hand)
    else:
        hand_categories[0].append(hand)

def total(hand_categories):
    sort_hands(hand_categories)
    winnings = 0
    rank = 1
    for cat in hand_categories:
        for hand in cat:
            winnings += (int(hand[1]) * rank)
            rank += 1
    return winnings

with open("advent7.txt", "r") as f:

    # Part 1

    hands = [line.split(" ") for line in f.read().splitlines()]
    hand_categories = [[], [], [], [], [], [], []]
    totals = {}
    for hand in hands:
        # Hack so we can ASCII value sort
        hand[0] = hand[0].replace("A", "E").replace("T", "A")\
        .replace("J", "B").replace("Q", "C").replace("K", "D")
        totals.clear()
        hand_data = find_hand_type(hand, totals)
        categorize(hand, hand_data, hand_categories)
    print(f"part 1: {total(hand_categories)}")

    # Part 2

    hand_categories = [[], [], [], [], [], [], []]
    for hand in hands:
        # Slightly different hack, we now want jokers weak
        hand[0] = hand[0].replace("B", "1")
        totals.clear()
        hand_data = find_hand_type(hand, totals, True)
        categorize(hand, hand_data, hand_categories)
    print(f"part 2: {total(hand_categories)}")