# PART 1; 10 minutes, incl. refactor

def next_sequence(old_sequence):
    new_sequence = []
    for i in range(len(old_sequence) - 1):
        new_sequence.append(old_sequence[i + 1] - old_sequence[i])

    for n in new_sequence:
        if n != 0:
            return new_sequence[-1] + next_sequence(new_sequence)
    return 0


res = 0
with open("2023_09.input") as f:
    for l in f.readlines():
        seq = [int(n) for n in l.strip().split(" ")]
        res += seq[-1] + next_sequence(seq)
print(res)


# PART 2; 25 min, very ugly code follows

def next_sequence(old_sequence, final_seq):
    new_sequence = []
    for i in range(len(old_sequence) - 1):
        new_sequence.append(old_sequence[i + 1] - old_sequence[i])

    final_seq.append(new_sequence)
    for n in new_sequence:
        if n != 0:
            return next_sequence(new_sequence, final_seq)
    return 0


res = 0
with open("2023_09.input") as f:
    for l in f.readlines():
        final_seq = []
        seq = [int(n) for n in l.strip().split(" ")]
        next_sequence(seq, final_seq)
        final_seq = [seq] + final_seq
        tmp = 0
        for i in range(len(final_seq)):
            tmp = final_seq[-i - 1][0] - tmp
        res += tmp

    print(res)

