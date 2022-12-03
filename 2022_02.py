# PART 1
def match1(opponent, chosen):
    if opponent == "A":
        if chosen == "X":
            return 3
        if chosen == "Y":
            return 6
        return 0
    if opponent == "B":
        if chosen == "X":
            return 0
        if chosen == "Y":
            return 3
        return 6
    if chosen == "X":
        return 6
    if chosen == "Y":
        return 0
    return 3


score = 0
chosen_vals = {"X": 1, "Y": 2, "Z": 3}
with open("2022_12_02.input") as f:
    for l in f.readlines():
        opponent, chosen = l.split()
        score += chosen_vals[chosen]
        score += match1(opponent, chosen)
print(score)


# PART 2
def match2(opponent, chosen):
    if opponent == "A":
        if chosen == "X":
            return 3
        if chosen == "Y":
            return 1
        return 2
    if opponent == "B":
        if chosen == "X":
            return 1
        if chosen == "Y":
            return 2
        return 3
    if chosen == "X":
        return 2
    if chosen == "Y":
        return 3
    return 1


score = 0
chosen_res = {"X": 0, "Y": 3, "Z": 6}
with open("2022_12_02.input") as f:
    for l in f.readlines():
        opponent, chosen = l.split()
        score += chosen_vals[chosen]
        score += match2(opponent, chosen)
print(score)
