# PART 1; took 45 minutes. Had to debug: 
# - sort line/hands and check specific positions instead of using Counter
# - raw_hand_card_value providing the Counter var instead of the raw line
# - rank_card not doing elif, just if (earlier versions just returned...)


from collections import Counter
import sys

sys.set_int_max_str_digits(10000)

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

def raw_hand_card_value(raw_hand):
    res = 0
    for idx, card in enumerate(reversed(raw_hand)):
        res += strength[card] * (100 ** (idx + 1))
    return res


def rank_card(line):
    # N.b. inefficient use of such big ints (10**700...) but easy to debug.
    # Would be more elegant to use hex instead and less digits with powers here.
    hand = Counter(line.strip().split(" ")[0])
    res = 10
    if hand.most_common()[0][1] == 5:  # 5 kind
        res **= 700
    elif hand.most_common()[0][1] == 4:  # 4 kind
        res **= 600
    elif hand.most_common()[0][1] == 3 and hand.most_common()[1][1] == 2:  # full
        res **= 500
    elif hand.most_common()[0][1] == 3:  # 3 kind
        res **= 400
    elif hand.most_common()[0][1] == 2 and hand.most_common()[1][1] == 2:  # 2 pair
        res **= 300
    elif hand.most_common()[0][1] == 2:  # pair
        res **= 200
    else:  # highest card
        res **= 100

    return res + raw_hand_card_value(line.strip().split(" ")[0])


with open("2023_07.input") as f:
    lines = f.readlines()
    sorted_lines = sorted(lines, key=rank_card)
    res = 0
    for idx, l in enumerate(sorted_lines):
        res += int(l.strip().split(" ")[1]) * (idx + 1)
    print(res)
