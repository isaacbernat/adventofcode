# PART 1 (took me almost 15 minutes... had to refresh regex library keywords ^_^U)
import re

vals = []

blue_pattern = r" (\d+) blue"
red_pattern = r" (\d+) red"
green_pattern = r" (\d+) green"


with open("2023_02.input") as f:
    res = 0
    for l in f.readlines():
        game_number, draws = l[5:].split(':')
        for d in draws.split(';'):
            units = re.search(blue_pattern, d)
            if units and int(units.group(1)) > 14:
                break
            units = re.search(red_pattern, d)
            if units and int(units.group(1)) > 12:
                break
            units = re.search(green_pattern, d)
            if units and int(units.group(1)) > 13:
                break
        else:
            res += int(game_number)
    print(res)

