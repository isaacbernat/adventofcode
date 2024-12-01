# PART 1; 25 min, my regex are still rusty...

import re


with open("2023_08.input") as f:
    lines = f.readlines()

instructions = lines[0].strip().replace('L', '0').replace('R', '1')
res = 0
current = "AAA"
paths = {}
line_pattern = r"^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)\n{0,1}"

for l in lines[2:]:
    origin, left, right = re.search(line_pattern, l).groups()    
    paths[origin] = (left, right)

while current != "ZZZ":
    current = paths[current][int(instructions[res % len(instructions)])]
    res += 1

print(res)


# PART 2 MCM (considered caching... still too slow)
from math import lcm


with open("2023_08.input") as f:
    lines = f.readlines()

instructions = lines[0].strip().replace('L', '0').replace('R', '1')
res = []
paths = {}
line_pattern = r"^([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)\n{0,1}"

for l in lines[2:]:
    origin, left, right = re.search(line_pattern, l).groups()
    paths[origin] = (left, right)
current = [p for p in paths.keys() if p[-1] == 'A']

for c in current:
    idx = 0
    while c[-1] != 'Z':
        c = paths[c][int(instructions[idx % len(instructions)])]
        idx += 1
    res.append(idx)
print(lcm(*res))


# PART 2 'brute-force' approach took 6 min
# import re


# with open("2023_08.input") as f:
#     lines = f.readlines()

# instructions = lines[0].strip().replace('L', '0').replace('R', '1')
# res = 0
# current = []
# paths = {}
# line_pattern = r"^([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)\n{0,1}"

# for l in lines[2:]:
#     origin, left, right = re.search(line_pattern, l).groups()
#     paths[origin] = (left, right)
# current = [p for p in paths.keys() if p[-1] == 'A']

# while len(current) != len([c for c in current if c[-1] == 'Z']):
#     current = [paths[c][int(instructions[res % len(instructions)])] for c in current]
#     res += 1
#     if res % 100 == 0:
#         print(res)

# print(res)
