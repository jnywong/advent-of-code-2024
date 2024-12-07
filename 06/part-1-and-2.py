def get_guard_path(position, direction, n_data):
    i = 0
    d = direction[i]
    path = [[position, d]]
    loop = False
    while 0 <= position[0] < len(data) and 0 <= position[1] < len(data):
        position = [position[0] + d[0], position[1] + d[1]]
        if position in obstruction:
            i += 1
            d = direction[i % len(direction)]
            position = path[-1][0]
        else:
            path.append([position, d])
        if [position, d] in path[:-2] or len(path) > 4 * n_data**2:
            loop = True
            return path, loop
    return path, loop


data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line)

obstruction = []
for i in range(len(data)):
    for j in range(len(data)):
        if "#" == data[i][0][j]:
            obstruction.append([i, j])
    if "^" in data[i][0]:
        y = data[i][0].index("^")
        x = i
        position = [x, y]

# Part 1
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
i = 0
d = direction[i]
path, loop = get_guard_path(position, direction, len(data))
path.pop()  # remove case that breaks while loop

unique = [list(p) for p in set(tuple(p[0]) for p in path)]
print(f"Part 1: {len(unique)}")

# Part 2

count_loop = 0
for p in unique:
    obstruction.append(p)
    new_path, loop = get_guard_path(position, direction, len(data))
    if loop:
        count_loop += 1
    obstruction.pop()
print(f"Part 2: {count_loop}")
