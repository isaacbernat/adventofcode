# PART 1
maxim = 0
with open("2022_12_01a.input") as f:
    current = 0
    for l in f.readlines():
        try:
            current += int(l)
        except:
            maxim = max(maxim, current)
            current = 0
print(maxim)


# PART 2
maxims = []
with open("2022_12_01a.input") as f:
    current = 0
    for l in f.readlines():
        try:
            current += int(l)
        except:
            maxims.append(current)
            current = 0
print(sum(sorted(maxims)[-3:]))
