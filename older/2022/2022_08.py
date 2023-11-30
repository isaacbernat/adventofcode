from pprint import pprint
from collections import defaultdict

# PART 1
def read_input():
    with open("2022_08.input") as f:
        trees = []
        for l in f.readlines():
            trees.append([int(a) for a in l.strip()])
        return trees


def initial_visibility(trees):
    visibility = []
    for line in trees:
        visibility.append([0 for l in line])

    for x in range(len(visibility)):
        visibility[x][0] = 1
        visibility[x][-1] = 1

    for y in range(len(visibility)):
        visibility[0][y] = 1
        visibility[-1][y] = 1
    return visibility


def is_visible(index_x, index_y, trees):
    val = trees[index_x][index_y]
    for index, tree in enumerate(trees[index_x]):
        if index >= index_y:
            return 1
        if tree >= val:
            break

    for i in range(1, len(trees[index_x])):
        if len(trees[index_x]) - i <= index_y:
            return 1
        if trees[index_x][- i] >= val:
            break

    for i in range(len(trees)):
        if i >= index_x:
            return 1
        if trees[i][index_y] >= val:
            break

    for i in range(1, len(trees)):
        if len(trees) - i <= index_x:
            return 1
        if trees[- i][index_y] >= val:
            break
    return 0


def total(visibility):
    res = 0
    for line in visibility:
        for v in line:
            res += v
    return res


trees = read_input()
visibility = initial_visibility(trees)

for index_x, line in enumerate(visibility):
    for index_y, tree in enumerate(line):
        if tree == 0:
            visibility[index_x][index_y] = is_visible(index_x, index_y, trees)

print(total(visibility))


# PART 2
def get_scene(index_x, index_y, trees):
    val = trees[index_x][index_y]
    left = right = up = down = 0

    for i in range(1, index_y + 1):
        left += 1
        if trees[index_x][index_y - i] >= val:
            break

    for i in range(1, len(trees[index_x]) - index_y):
        right += 1
        if trees[index_x][index_y + i] >= val:
            break

    for i in range(1, index_x + 1):
        up += 1
        if trees[index_x - i][index_y] >= val:
            break

    for i in range(1, len(trees) - index_x):
        down += 1
        if trees[index_x + i][index_y] >= val:
            break

    return left * right * up * down


best = 0
for index_x, line in enumerate(trees):
    if index_x == 0 or index_x == len(trees) -1:
        continue
    for index_y, tree in enumerate(line):
        if index_y == 0 or index_y == len(line) -1:
            continue
        best = max(best, get_scene(index_x, index_y, trees))

print(best)
