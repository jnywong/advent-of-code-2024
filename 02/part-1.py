data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append([int(i) for i in line])

n_safe = 0
for report in data:
    diff = [report[j + 1] - report[j] for j in range(len(report) - 1)]
    if all(d > 0 for d in diff) or all(d < 0 for d in diff):
        diff_abs = [abs(d) for d in diff]
        check_diff = all(d >= 1 for d in diff_abs) and all(d <= 3 for d in diff_abs)
        if check_diff:
            n_safe += 1
