def get_guard_path(position, direction, n_data):
    i = 0
    d = direction[i]
    path = [position]
    loop = False
    while 0 <= position[0] < len(data) and 0 <= position[1] < len(data):
        position = [position[0] + d[0], position[1] + d[1]]
        if position in obstruction:
            i += 1
            d = direction[i % len(direction)]
            position = path[-1]
        else:
            path.append(position)
        if is_loop(path) or len(path) > 4 * n_data**2:
            loop = True
            return path, loop
    return path, loop


def is_loop(path):
    return any(path[-i:] == path[-2 * i : -i] for i in range(2, len(path) // 2 + 1))


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
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 0
d = direction[i]
path, loop = get_guard_path(position, direction, len(data))
path.pop()  # remove case that breaks while loop

unique = [list(p) for p in set(tuple(p) for p in path)]
print(f"Part 1: {len(unique)}")

# Part 2

# path = [[6, 3]]
loop_pos = []
for p in path:
    obstruction.append(p)
    new_path, loop = get_guard_path(position, direction, len(data))
    if loop:
        # print(f"{p}")
        loop_pos.append(p)
        # print(new_path)
    obstruction.pop()
unique_loop_pos = [list(l) for l in set(tuple(l) for l in loop_pos)]
print(f"Part 2: {len(unique_loop_pos)}")
