example_readings = ["5483143223", "2745854711", "5264556173", "6141336146", "6357385478", "4167524645", "2176841721", "6882881134", "4846848554", "5283751526"]
readings = ["3172537688", "4566483125", "6374512653", "8321148885", "4342747758", "1362188582", "7582213132", "6887875268", "7635112787", "7242787273"]

rows = len(readings) + 2
columns = len(readings[0]) + 2


# PART 1
def debug_print(lines):
    for line in lines:
        print([n for n in line if n > -9])


def build_wall_and_convert_to_int(lines):
    new_lines = ["Z" * (columns)]
    for line in lines:
        new_lines.append(f"Z{line}Z")
    new_lines.append("Z" * (columns))
    return [[int(c) if c != "Z" else -9 for c in line] for line in new_lines]


def increase_energy(lines):
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            if n >= 0:
                lines[i][j] += 1
    return lines


def flash(lines):
    flashes = 0
    new_flashes = 0
    for i in range(rows):
        for j in range(columns):
            if (lines[i][j] > 9):
                increase_flash(i, j, lines)
                new_flashes += 1

    flashes += new_flashes
    if new_flashes:
        flashes += flash(lines)
    return flashes


def increase_flash(i, j, lines):
    if lines[i - 1][j - 1] >= 0:
        lines[i - 1][j - 1] += 1
    if lines[i - 1][j] >= 0:
        lines[i - 1][j] += 1
    if lines[i - 1][j + 1] >= 0:
        lines[i - 1][j + 1] += 1

    if lines[i][j - 1] >= 0:
        lines[i][j - 1] += 1
    lines[i][j] = -1
    if lines[i][j + 1] >= 0:
        lines[i][j + 1] += 1

    if lines[i + 1][j - 1] >= 0:
        lines[i + 1][j - 1] += 1
    if lines[i + 1][j] >= 0:
        lines[i + 1][j] += 1
    if lines[i + 1][j + 1] >= 0:
        lines[i + 1][j + 1] += 1


def reset_energy(lines):
    for i in range(rows):
        for j in range(columns):
            if lines[i][j] == -1:
                lines[i][j] = 0
    return lines


flashes = 0
steps = 100
lines = build_wall_and_convert_to_int(readings)

for i in range(steps):
    lines = increase_energy(lines)
    flashes += flash(lines)
    lines = reset_energy(lines)

print(flashes)


# PART 2
def reset_energy_with_sync(lines):
    all_minus = True
    for i in range(rows):
        for j in range(columns):
            if lines[i][j] >= 0:
                all_minus = False
            if lines[i][j] == -1:
                lines[i][j] = 0
    return lines, all_minus


sync = False
flashes = 0
steps = 1000
lines = build_wall_and_convert_to_int(readings)

for i in range(steps):
    lines = increase_energy(lines)
    flashes += flash(lines)
    lines, sync = reset_energy_with_sync(lines)
    if sync:
        print(i + 1)
        break
