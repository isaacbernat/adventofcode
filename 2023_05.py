# PART 1; took 12 minutes. But part 0 (below) took 40m... 
def use_maps(idx, lines, target):
    new_target = target
    while lines[idx].strip() if idx < len(lines) else 0:
        line = [int(e) for e in lines[idx].strip().split(" ")]
        if target >= line[1] and target < line[1] + line[2]:
            new_target = line[0] + target - line[1]
        idx += 1
    return idx, new_target


digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
res = []
maps = []
with open("2023_05.input") as f:
    lines = f.readlines()
    seeds = [int(seed) for seed in lines[0].split(" ")[1:]]

    for s in seeds:
        idx = 3
        target = s
        while(idx < len(lines)):
            idx, target = use_maps(idx, lines, target)
            idx += 2
        res.append(target)
    print(min(res))


# # PART 0; Q&D version which only works for small numbers
# def build_maps(idx, lines):
#     map_index = {}
#     while lines[idx].strip() if idx < len(lines) else 0:
#         line = [int(e) for e in lines[idx].strip().split(" ")]
#         for i in range(0, line[2]):
#             map_index[line[1] + i] = line[0] + i
#         idx += 1
#     return idx, map_index


# def calc_endvals(seed, maps):
#     for m in maps:
#         try:
#             seed = m[seed]
#         except:
#             continue
#     return seed


# digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# res = []
# maps = []
# idx = 3
# with open("2023_05.input") as f:
#     lines = f.readlines()
#     seeds = [int(seed) for seed in lines[0].split(" ")[1:]]

#     while(idx < len(lines)):
#         idx, new_map = build_maps(idx, lines)
#         maps.append(new_map)
#         idx += 2

#     for s in seeds:
#         res.append(calc_endvals(s, maps))

#     print(min(res))
