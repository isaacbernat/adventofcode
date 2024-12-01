# PART 1; took 12 minutes. But part 0 (below) took 40m... 
def use_maps(idx, lines, target):
    new_target = target
    while lines[idx].strip() if idx < len(lines) else 0:
        line = [int(e) for e in lines[idx].strip().split(" ")]
        if target >= line[1] and target < line[1] + line[2]:
            new_target = line[0] + target - line[1]
        idx += 1
    return idx, new_target


res = []
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


# PART 2; took hours. Debugging inputs line by line because of a bad assigment
def use_ranged_maps(idx, lines, targets):
    new_targets = []
    final_index = idx
    while lines[final_index].strip() if final_index < len(lines) else 0:
        final_index += 1

    for t in targets:
        tini, tend = t
        for l in lines[idx:final_index]:
            line = [int(e) for e in l.strip().split(" ")]
            max_target = line[1] + line[2]

            if tini >= line[1] and tini < max_target:
                new_ini = line[0] + tini - line[1]
                if tini + tend > max_target:
                    remain_end = (tini + tend) - (max_target)
                    new_end = tend - remain_end
                    targets.append((max_target, remain_end))
                else:
                    new_end = tend
                new_targets.append((new_ini, new_end))
                break
        else:  # if there's no matching rule
            new_targets.append((tini, tend))
    return final_index + 2, new_targets


res = []
with open("2023_05.input") as f:
    lines = f.readlines()
    seeds = [int(seed) for seed in lines[0].split(" ")[1:]]

    for i in range(len(seeds)//2):
        idx = 3
        targets = [(seeds[i * 2], seeds[i * 2 + 1])]
        while(idx < len(lines)):
            idx, targets = use_ranged_maps(idx, lines, targets)
        res.append(targets)

    minimal = res[0][0][0]
    for seed_ranges in res:
        for rang in seed_ranges:
            minimal = min(rang[0], minimal)
    print(minimal)


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


# res = []
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
