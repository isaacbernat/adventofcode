# PART 1. 31 min
import sys
sys.setrecursionlimit(20000)


def next_pos(pipes, x, y, direction):
    # print(f"pipes{pipes[y][x]} x{x} y{y} direction{direction} steps{steps}")
    current = pipes[y][x]
    if current == 'S':
        return 1
    if current == '|':
        y = y + 1 if direction == 'S' else y - 1 
    elif current == '-':
        x = x + 1 if direction == 'W' else x - 1 
    elif current == 'L':
        if direction == 'S':
            direction = 'W'
            x += 1
        else:
            direction = 'N'
            y -= 1
    elif current == 'J':
        if direction == 'S':
            direction = 'E'
            x -= 1
        else:
            direction = 'N'
            y -= 1
    elif current == '7':
        if direction == 'N':
            direction = 'E'
            x -= 1
        else:
            direction = 'S'
            y += 1
    elif current == 'F':
        if direction == 'N':
            direction = 'W'
            x += 1
        else:
            direction = 'S'
            y += 1
    return next_pos(pipes, x, y, direction) + 1


res = 0
init_direction = 'N'
init_x, init_y = 110, 119
with open("2023_10.input") as f:
    lines = f.readlines()

print(next_pos(lines, init_x, init_y, init_direction) // 2)
