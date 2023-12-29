# PART 1; 10 minutes, incl. refactor


def next_sequence(old_sequence):
    new_sequence = []
    for i in range(len(old_sequence) - 1):
        new_sequence.append(old_sequence[i + 1] - old_sequence[i])

    for n in new_sequence:
        if n != 0:
            return new_sequence[-1] + next_sequence(new_sequence)
    return new_sequence[-1]


res = 0
with open("2023_09.input") as f:
    for l in f.readlines():
        seq = [int(n) for n in l.strip().split(" ")]
        res += seq[-1] + next_sequence(seq)
print(res)
