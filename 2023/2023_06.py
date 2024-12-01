# PART 1; 16 min
def calc_distance(speed, time_left):
    return speed * time_left


def better_times(time, distance):
    res = 0
    for t in range(time):
        if calc_distance(t, time - t) > distance:
            res += 1
    return res


with open("2023_06.input") as f:
    lines = f.readlines()
times = [int(seed) for seed in lines[0].strip().split(" ")[1:] if seed]
distances = [int(seed) for seed in lines[1].strip().split(" ")[1:] if seed]

res = 1
for i in range(len(times)):
    res *= better_times(times[i], distances[i])
print(res)


# PART 1B; I refactored above code to use reduce
from functools import reduce
def better_times(time, distance):
    return reduce(lambda x, y: x + (y * (time - y) > distance), range(time))

with open("2023_06.input") as f:
    lines = f.readlines()
times = [int(seed) for seed in lines[0].strip().split(" ")[1:] if seed]
distances = [int(seed) for seed in lines[1].strip().split(" ")[1:] if seed]

print(reduce(lambda x, y: x * better_times(times[y], distances[y]), range(len(times)), 1))


# PART 2; 3 min
with open("2023_06.input") as f:
    lines = f.readlines()
time = int(lines[0].strip().replace(" ", "").split(":")[1])
distance = int(lines[1].strip().replace(" ", "").split(":")[1])
print(better_times(time, distance))
