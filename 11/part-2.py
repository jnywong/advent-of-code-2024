from functools import cache


@cache
def count(d, b=75):
    if b == 0:
        return 1
    if d == 0:
        return count(1, b - 1)

    length = len(str(d))
    if length % 2:
        return count(d * 2024, b - 1)

    print(d // 10 ** (length // 2))

    return count(d // 10 ** (length // 2), b - 1) + count(
        d % 10 ** (length // 2), b - 1
    )


data = []
with open("input.txt", "r") as file:
    data = file.read()

data = map(int, data.split())
print(sum(map(count, data)))
