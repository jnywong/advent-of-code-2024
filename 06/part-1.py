data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line)

obstruction = []
for i in range(len(data)):
    for j in range(len(data)):
        print(data[i])
        if "#" == data[i][0][j]:
            obstruction.append([i, j])
    if "^" in data[i][0]:
        y = data[i][0].index("^")
        x = i
        position = [x, y]

flag = False
path = [position]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0
d = direction[i]
while 0 <= position[0] < len(data) and 0 <= position[1] < len(data):
    position = [position[0] + d[0], position[1] + d[1]]
    if position in obstruction:
        i += 1
        d = direction[i % len(direction)]
        position = path[-1]
    else:
        path.append(position)

unique = [list(p) for p in set(tuple(p) for p in path)]
print(len(unique) - 1)  # remove case that breaks while loop
