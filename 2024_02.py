# PART 1
safe_reports = 0
with open("2024_02.input") as f:
    for report in f.readlines():
        levels = [int(l) for l in report.split(" ")]
        increasing_trend = levels[0] < levels[1]
        prev = levels[0]
        for l in levels[1:]:
            if (
                (abs(prev - l) > 3) or
                (prev == l) or
                (prev > l and increasing_trend) or 
                (prev < l and not increasing_trend)
                ):
                prev = -1
                break
            prev = l
        safe_reports += prev != -1
print(safe_reports)


# PART 2, has some code repetition, but imho it's acceptable and easy to follow
def is_invalid_pair(prev, curr, increasing_trend):
    return (
        (abs(prev - curr) > 3) or
        (prev == curr) or
        (prev > curr and increasing_trend) or
        (prev < curr and not increasing_trend)
    )


safe_reports = 0
with open("2024_02.input") as f:
    for report in f.readlines():
        levels = [int(l) for l in report.split(" ")]
        increasing_trend = levels[0] < levels[1]
        prev = levels[0]
        warning = -1
        for i, l in enumerate(levels[1:], 1):
            if is_invalid_pair(prev, l, increasing_trend):
                if warning != -1:
                    prev = -1
                    break
                warning = i
            else:
                prev = l
        if prev == -1 and warning in [1, 2]:  # remove the 1st element and try again
            increasing_trend = levels[1] < levels[2]
            prev = levels[1]
            for l in levels[2:]:
                if is_invalid_pair(prev, l, increasing_trend):
                    prev = -1
                    warning = i
                    break
                else:
                    prev = l
        if prev == -1 and warning in [2, 3]:  # remove the 2nd element and try again
            increasing_trend = levels[0] < levels[2]
            prev = levels[0]
            for l in levels[2:]:
                if is_invalid_pair(prev, l, increasing_trend):
                    prev = -1
                    warning = i  # not needed, but kept for consistency
                    break
                else:
                    prev = l
        safe_reports += prev != -1
print(safe_reports)
