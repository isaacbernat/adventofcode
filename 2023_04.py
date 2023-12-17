# PART 1; 25 min... wasted a lot of time with non-matching end_line chars...
def get_numbers_line(line):
    winners, numbers = line.split(":")[1].split("|")
    w = {w for w in winners.strip().split(" ") if w}
    n = {n for n in numbers.strip().split(" ") if n}
    return w, n, -1


res = 0
with open("2023_04.input") as f:
    for l in f.readlines():
        numbers, winners, cnt = get_numbers_line(l)
        for n in numbers:
            cnt += 1 if n in winners else 0
        res += 2 ** cnt if cnt >= 0 else 0

print(res)
