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
