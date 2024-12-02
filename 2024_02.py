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
