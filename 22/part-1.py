import math
from multiprocessing import Pool


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def evolve(a):
    a = prune(mix(64 * a, a))
    a = prune(mix(math.floor(a / 32), a))
    a = prune(mix(2048 * a, a))
    return a


if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        for line in f:
            data.append(int(line.split()[0]))

    n = 2000
    p = Pool()
    for i in range(n):
        data = p.map(evolve, data)
    print(sum(data))
