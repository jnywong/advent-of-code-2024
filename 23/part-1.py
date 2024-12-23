from itertools import combinations


data = []
computer, connection = set(), set()
with open("input.txt", "r") as f:
    for line in f:
        a, b = line.strip().split("-")
        computer.update([a, b])
        connection.update([(a, b), (b, a)])

print(
    sum(
        {(a, b), (b, c), (c, a)} < connection and "t" in (a + b + c)[::2]
        for a, b, c in combinations(computer, 3)
    )
)
