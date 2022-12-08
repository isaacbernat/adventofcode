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


def is_visible(x, y, trees):
    val = trees[index_x][index_y]
    for index, tree in enumerate(trees[index_x]):
        if index > index_y:
            break
        if tree < val:
            return 1

    for index, tree in enumerate(list(reversed(trees[index_x]))):
        if index < index_y:
            break
        if tree < val:
            return 1

    for i in range(len(trees)):
        if i > index_x:
            break
        if trees[i][index_y] < val:
            return 1

    for i in range(len(trees)):
        if len(trees) - i - 1 < index_x:
            break
        if trees[len(trees) - i - 1][index_y] < val:
            return 1
    return 0


def total(visibility):
    res = 0
    for line in visibility:
        for v in line:
            res += v
    return res


trees = read_input()
visibility = initial_visibility(trees)
pprint(visibility)

for index_x, line in enumerate(visibility):
    for index_y, tree in enumerate(line):
        if tree == 0:
            visibility[index_x][index_y] = is_visible(index_x, index_y, trees)

# ~20 min WIP

print(total(visibility))
pprint(trees)
pprint(visibility)