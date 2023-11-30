# PART 1
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
with open("2022_03.input") as f:
    for l in f.readlines():
        init, end = l[:int(len(l)/2)], l[int(len(l)/2):]
        common = get_common(init, end)
        score += get_val(common)
print(score)


# PART 2
def get_common3(A, B, C):
    setB, setC = set(B), set(C)
    for item in A:
        if item in setB and item in setC:
            return item


def get_val(char):
    if char == char.upper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


score = 0
chosen_res = {"X": 0, "Y": 3, "Z": 6}
with open("2022_03.input") as f:
    try:
        while(True):
            l1, l2, l3 = f.readline(), f.readline(), f.readline()
            common = get_common3(l1, l2, l3)
            score += get_val(common)
    except:
        print(score)
