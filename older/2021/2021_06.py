example_readings = [3,4,3,1,2]
readings = [2,1,1,4,4,1,3,4,2,4,2,1,1,4,3,5,1,1,5,1,1,5,4,5,4,1,5,1,3,1,4,2,3,2,1,2,5,5,2,3,1,2,3,3,1,4,3,1,1,1,1,5,2,1,1,1,5,3,3,2,1,4,1,1,1,3,1,1,5,5,1,4,4,4,4,5,1,5,1,1,5,5,2,2,5,4,1,5,4,1,4,1,1,1,1,5,3,2,4,1,1,1,4,4,1,2,1,1,5,2,1,1,1,4,4,4,4,3,3,1,1,5,1,5,2,1,4,1,2,4,4,4,4,2,2,2,4,4,4,2,1,5,5,2,1,1,1,4,4,1,4,2,3,3,3,3,3,5,4,1,5,1,4,5,5,1,1,1,4,1,2,4,4,1,2,3,3,3,3,5,1,4,2,5,5,2,1,1,1,1,3,3,1,1,2,3,2,5,4,2,1,1,2,2,2,1,3,1,5,4,1,1,5,3,3,2,2,3,1,1,1,1,2,4,2,2,5,1,2,4,2,1,1,3,2,5,5,3,1,3,3,1,4,1,1,5,5,1,5,4,1,1,1,1,2,3,3,1,2,3,1,5,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,1,5,2,4,5,5,1,1,5,1,5,5,1,1,3,3,1,1,3,1]


# PART 1
def calculate_fish(days_til_hatch, days_left):
    if days_til_hatch >= days_left:
        return 1
    days_left -= days_til_hatch
    return calculate_fish(7, days_left) + calculate_fish(9, days_left)


total_fish = 0
total_days = 80
for days in readings:
    fish_count = calculate_fish(days, total_days)
    total_fish += fish_count

print(f"{total_fish}, {total_days}")


# PART 2
def calculate_fish_memo(days_til_hatch, days_left):
    if days_til_hatch >= days_left:
        return 1

    memo_key = (days_til_hatch, days_left)
    if memo_fish.get(memo_key):
        return memo_fish.get(memo_key)

    days_left -= days_til_hatch
    memo_fish[memo_key] = calculate_fish_memo(7, days_left) + calculate_fish_memo(9, days_left)
    return memo_fish[memo_key]


memo_fish = {}
total_days = 256
total_fish = 0
for days in readings:
    fish_count = calculate_fish_memo(days, total_days)
    total_fish += fish_count

print(f"{total_fish}, {total_days}")
