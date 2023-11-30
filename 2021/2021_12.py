import string
from collections import defaultdict
import copy

small_caves = {a for a in string.ascii_lowercase}
big_caves = {a for a in string.ascii_uppercase}
valid_paths = 0

example_readings = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
example_readings2 = ["dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"]
example_readings3 = ["fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he", "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"]
readings = ["qi-UD", "jt-br", "wb-TF", "VO-aa", "UD-aa", "br-end", "end-HA", "qi-br", "br-HA", "UD-start", "TF-qi", "br-hf", "VO-hf", "start-qi", "end-aa", "hf-HA", "hf-UD", "aa-hf", "TF-hf", "VO-start", "wb-aa", "UD-wb", "KX-wb", "qi-VO", "br-TF", ]

# readings = example_readings3


# PART 1
def build_graph(inp):
    graph = defaultdict(list)
    for ori, dest in [pair.split("-") for pair in inp]:
        graph[ori].append(dest)
        graph[dest].append(ori)
    return graph


def explore_path(graph, dest):
    global valid_paths
    paths = []
    new_graph = copy.deepcopy(graph)
    if dest[0] in small_caves:
        paths = new_graph.pop(dest, [])
    elif dest[0] in big_caves:
        paths = new_graph.get(dest, [])
    for p in paths:
        if p == "end":
            valid_paths += 1
        else:
            explore_path(new_graph, p)


valid_paths = 0
init_graph = build_graph(readings)
for dest in init_graph.pop("start"):
    explore_path(init_graph, dest)

print(valid_paths)


# PART 2
