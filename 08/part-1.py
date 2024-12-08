import itertools


def get_distance(f1, f2):
    dx = abs(f1[0] - f2[0])
    dy = abs(f1[1] - f2[1])
    return dx, dy


data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line[0])

frequencies = set(f for d in data for f in d)
frequencies.remove(".")

map_antenna = [[] for _ in frequencies]
for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(frequencies)):
            if data[i][j] == list(frequencies)[k]:
                map_antenna[k].append((i, j))

antinodes = []
for m in map_antenna:
    pair = itertools.combinations(m, 2)
    for p1, p2 in pair:
        dx, dy = get_distance(p1, p2)
        if p1[1] < p2[1]:
            a1 = [p1[0] - dx, p1[1] - dy]
            a2 = [p2[0] + dx, p2[1] + dy]
        else:
            a1 = [p1[0] - dx, p1[1] + dy]
            a2 = [p2[0] + dx, p2[1] - dy]
        antinodes.append(a1)
        antinodes.append(a2)

antinodes = [a for a in antinodes if all(0 <= x < len(data) for x in a)]
unique = [list(a) for a in set(tuple(a) for a in antinodes)]
print(len(unique))
