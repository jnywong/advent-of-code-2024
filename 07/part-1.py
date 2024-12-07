import itertools


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line)

test_value = [int(v[0][:-1]) for v in data]
terms = [[int(v) for v in val[1:]] for val in data]
operators = [add, mul]

calibration = []
for i in range(len(test_value)):
    n_terms = len(terms[i])
    for ops in itertools.product(operators, repeat=n_terms - 1):
        j = 0
        result = [terms[i][j]] * n_terms
        for o in ops:
            result[j + 1] = o(result[j], terms[i][j + 1])
            j += 1
        if result[-1] == test_value[i]:
            calibration.append(test_value[i])
            break

print(sum(calibration))
