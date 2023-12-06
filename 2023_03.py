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


# PART 2 (1h+, So much time spent using re.search instead of findall ;_;)
def get_gear_ratios_per_line(x, lines):
    y = 1
    partial_res = 0
    while y < len(lines[x]) - 1:
        if lines[x][y] == '*':
            partial_res += gear_info(x, y, lines)
        y += 1
    return partial_res


def get_inline_number(y, line):
    debug_y = y
    for idx, num in enumerate(line[y:]):
        if num not in nums:
            y += idx
            break
    else:
        y = len(line)
    number_pattern = r"(\d+)"
    return re.findall(number_pattern, line[:y])[-1]


def gear_info(x, y, lines):
    number = []

    # same line
    char = lines[x][y - 1]
    if char in nums:
        number_pattern = r"(\d+)\*"
        number.append(re.findall(number_pattern, lines[x][:y + 1])[-1])
    char = lines[x][y + 1]
    if char in nums:
        number_pattern = r"\*(\d+)"
        number.append(re.findall(number_pattern, lines[x][y:])[0])

    # line above... ugly code... ^_^'
    skip_y = skip_y1 = False
    char = lines[x - 1][y - 1]
    if char in nums:
        if lines[x - 1][y] in nums:
            skip_y = True
            if lines[x - 1][y + 1] in nums:
                skip_y1 = True
        number.append(get_inline_number(y - 1, lines[x - 1]))

    char = lines[x - 1][y]
    if not skip_y and char in nums:
        if lines[x - 1][y + 1] in nums:
            skip_y1 = True
        number.append(get_inline_number(y, lines[x - 1]))
    char = lines[x - 1][y + 1]
    if not skip_y1 and char in nums:
        number.append(get_inline_number(y + 1, lines[x - 1]))

    # line below... ugly code... ^_^'
    skip_y = skip_y1 = False
    char = lines[x + 1][y - 1]
    if char in nums:
        if lines[x + 1][y] in nums:
            skip_y = True
            if lines[x + 1][y + 1] in nums:
                skip_y1 = True
        number.append(get_inline_number(y - 1, lines[x + 1]))
    char = lines[x + 1][y]
    if not skip_y and char in nums:
        if lines[x + 1][y + 1] in nums:
            skip_y1 = True
        number.append(get_inline_number(y, lines[x + 1]))
    char = lines[x + 1][y + 1]
    if not skip_y1 and char in nums:
        number.append(get_inline_number(y + 1, lines[x + 1]))

    if len(number) == 2:
        return int(number[0]) * int(number[1])
    return 0


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
        res += get_gear_ratios_per_line(n + 1, lines)
print(res)
