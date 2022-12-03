def get_common(A, B):
    setB = set(B)
    for item in A:
        if item in setB:
            return item


def get_val(char):
    if char == char.upper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


score = 0
chosen_res = {"X": 0, "Y": 3, "Z": 6}
with open("2022_12_03.input") as f:
    for l in f.readlines():
        init, end = l[:int(len(l)/2)], l[int(len(l)/2):]
        common = get_common(init, end)
        score += get_val(common)
print(score)
