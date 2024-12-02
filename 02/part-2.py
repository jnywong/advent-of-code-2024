# data = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append([int(i) for i in line])


def is_safe(report):
    diff = [report[j + 1] - report[j] for j in range(len(report) - 1)]
    if all(d > 0 for d in diff) or all(d < 0 for d in diff):
        diff_abs = [abs(d) for d in diff]
        check_diff = all(d >= 1 for d in diff_abs) and all(d <= 3 for d in diff_abs)
        if check_diff:
            return True
    return False


n_safe = sum(
    [
        any([is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))])
        for report in data
    ]
)

print(n_safe)
