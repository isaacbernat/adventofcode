# PART 1 (took me almost 40 minutes... but got it working on first attempt :D)
import re


def get_part_numbers_per_line(x, lines):
    y = 1
    partial_res = 0
    while y < len(lines[x]) - 1:
        if lines[x][y] not in nums:
            y += 1
            continue
        number, delta = get_number(x, y, lines)
        if is_part_number(x, y, lines):
            partial_res += number
        y += delta
    return partial_res


def get_number(x, y, lines):
    number_pattern = r"(\d+)."
    num = re.search(number_pattern, lines[x][y:]).group(1)
    return int(num), len(num)


def is_part_number(x, y, lines):  # ugly, but functional
    while(lines[x][y] in nums):
        char = lines[x - 1][y]
        if char not in nums and char != '.':
            return True
        char = lines[x + 1][y]
        if char not in nums and char != '.':
            return True
        char = lines[x][y - 1]
        if char not in nums and char != '.':
            return True
        char = lines[x][y + 1]
        if char not in nums and char != '.':
            return True

        # explore diagonals
        char = lines[x - 1][y - 1]
        if char not in nums and char != '.':
            return True
        char = lines[x - 1][y + 1]
        if char not in nums and char != '.':
            return True
        char = lines[x + 1][y - 1]
        if char not in nums and char != '.':
            return True
        char = lines[x + 1][y + 1]
        if char not in nums and char != '.':
            return True

        y += 1
    return False


lines = []
res = 0
nums = '0123456789'

with open("2023_03.input") as f:
    # preprocess input 
    first = 1
    for l in f.readlines():
        if first:
            lines.append('.' * (len(l) + 1))
            first = 0
        lines.append(f'.{l.strip()}.')
    else:
        lines.append(lines[0])

    for n in range(len(lines) - 1):
        res += get_part_numbers_per_line(n + 1, lines)
print(res)
