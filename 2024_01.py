# PART 1
lines, coords0, coords1 = [], [], []
with open("2024_01.input") as f:
    lines = f.readlines()

for l in lines:
    line = l.split("   ")
    coords0.append(int(line[0]))
    coords1.append(int(line[1]))

coords0.sort()
coords1.sort()
total_distance = 0
for i in range(len(lines)):
    total_distance += abs(coords0[i] - coords1[i])
print(total_distance)


# PART 2
from collections import defaultdict
similarity = defaultdict(int)
for i in range(len(lines)):
    similarity[coords1[i]] += 1

similarity_score = {}
for k, v in similarity.items():
    similarity_score[k] = k*v

score = 0
for c0 in coords0:
    score += similarity_score.get(c0, 0)
print(score)
