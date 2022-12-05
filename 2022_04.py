# PART 1
def are_contained(a, b):
    ranges_a, ranges_b = a.split("-"), b.split("-")
    return (
        (int(ranges_a[0]) <= int(ranges_b[0]) and int(ranges_a[1]) >= int(ranges_b[1])) or
        (int(ranges_a[0]) >= int(ranges_b[0]) and int(ranges_a[1]) <= int(ranges_b[1]))
    )


contained = 0
with open("2022_04.input") as f:
    for l in f.readlines():
        assignments = l.split(",")
        if are_contained(assignments[0], assignments[1]):
            contained += 1
print(contained)


# PART 2
def do_overlap(a, b):  # v1 O(N) mem
    ranges_a, ranges_b = a.split("-"), b.split("-")
    values_a = [i for i in range(int(ranges_a[0]), int(ranges_a[1]) + 1)]
    values_b = set([i for i in range(int(ranges_b[0]), int(ranges_b[1]) + 1)])
    for a in values_a:
        if a in values_b:
            return True
    return False


def do_overlap(a, b):  # v2 O(1) mem
    ranges_a, ranges_b = a.split("-"), b.split("-")
    min_b, max_b = int(ranges_b[0]), int(ranges_b[1])
    for a in range(int(ranges_a[0]), int(ranges_a[1]) + 1):
        if min_b <= a <= max_b:
            return True
    return False


overlap = 0
with open("2022_04.input") as f:
    for l in f.readlines():
        assignments = l.split(",")
        if do_overlap(assignments[0], assignments[1]):
            overlap += 1
print(overlap)
