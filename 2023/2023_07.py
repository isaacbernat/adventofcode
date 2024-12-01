# PART 1; took 45 minutes. Had to debug: 
# - sort line/hands and check specific positions instead of using Counter
# - raw_hand_card_value providing the Counter var instead of the raw line
# - rank_card not doing elif, just if (earlier versions just returned...)

from collections import Counter


strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

def calc_hand_type(hand):
    # N.b. inefficient use of large ints (10**700...) but easy to debug.
    # Would be more elegant to use hex instead + less digits with powers here.
    # Even better github.com/salt-die/Advent-of-Code/blob/main/2023/day_07.py
    # It didn't occur to me to use simple count to compare hand values...
    if hand.most_common()[0][1] == 5:  # 5 kind
        return 10 ** 700
    if hand.most_common()[0][1] == 4:  # 4 kind
        return 10 ** 600
    if hand.most_common()[0][1] == 3 and hand.most_common()[1][1] == 2:  # full
        return 10 ** 500
    if hand.most_common()[0][1] == 3:  # 3 kind
        return 10 ** 400
    if hand.most_common()[0][1] == 2 and hand.most_common()[1][1] == 2:  # 2 pair
        return 10 ** 300
    if hand.most_common()[0][1] == 2:  # pair
        return 10 ** 200
    return 10 ** 100  # highest card


def raw_hand_card_value(raw_hand):
    res = 0
    for idx, card in enumerate(reversed(raw_hand)):
        res += strength[card] * (100 ** (idx + 1))
    return res


def rank_card(line):
    hand = Counter(line.strip().split(" ")[0])
    res = calc_hand_type(hand)
    return res + raw_hand_card_value(line.strip().split(" ")[0])


with open("2023_07.input") as f:
    lines = f.readlines()
    sorted_lines = sorted(lines, key=rank_card)
    res = 0
    for idx, l in enumerate(sorted_lines):
        res += int(l.strip().split(" ")[1]) * (idx + 1)
    print(res)


# PART 2: 7 minutes
strength["J"] = 1


def rank_card(line):
    hand = Counter(line.strip().split(" ")[0])

    most_common = hand.most_common()[0][0]
    if most_common == "J" and hand.most_common()[0][1] != 5:
        most_common = hand.most_common()[1][0]
    J_cards = hand.get("J", 0)
    if J_cards:
        hand.pop("J")
    hand[most_common] += J_cards

    res = calc_hand_type(hand)
    return res + raw_hand_card_value(line.strip().split(" ")[0])


with open("2023_07.input") as f:
    lines = f.readlines()
    sorted_lines = sorted(lines, key=rank_card)
    res = 0
    for idx, l in enumerate(sorted_lines):
        res += int(l.strip().split(" ")[1]) * (idx + 1)
    print(res)
