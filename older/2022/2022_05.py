# PART 1
def read_input():  # 20 min
    stacks = []
    is_first, is_crates = True, True
    instructions = []
    with open("2022_05.input") as f:
        for l in f.readlines():  # read stacks
            if is_crates:
                if is_first:
                    stacks = [[] for _ in range(int((len(l) + 1)/4))]
                    is_first = False

                if l[0] == '\n':
                    is_crates = False
                    continue
                if l[1] == "1":
                    continue

                for i in range(len(stacks)):
                    val = l[i * 4 + 1]
                    if val != " ":
                        stacks[i] += val
            else:  # if not is_crates:
                line = l.split(" ")
                instructions.append([int(line[1]), int(line[3]), int(line[5])])
    return stacks, instructions


def print_result(stack):  # 2 min
    print("".join([l[0] for l in stack]))


def process_instructions(stacks, instructions): # 10 min
    for i in instructions:
        stacks[i[2] - 1] = list(reversed(stacks[i[1] - 1][:i[0]])) + stacks[i[2] - 1]
        stacks[i[1] - 1] = stacks[i[1] - 1][i[0]:]
    return stacks


stacks, instructions = read_input()
stacks = process_instructions(stacks, instructions)
print_result(stacks)


# PART 2
def process_instructions(stacks, instructions): # <1 min
    for i in instructions:
        stacks[i[2] - 1] = stacks[i[1] - 1][:i[0]] + stacks[i[2] - 1]
        stacks[i[1] - 1] = stacks[i[1] - 1][i[0]:]
    return stacks


stacks, instructions = read_input()
stacks = process_instructions(stacks, instructions)
print_result(stacks)
