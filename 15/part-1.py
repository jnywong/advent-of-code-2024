direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def parse_move(data):
    move = []
    for i in range(len(data)):
        if data[i] == ">":
            move.append(direction[0])
        elif data[i] == "<":
            move.append(direction[1])
        elif data[i] == "^":
            move.append(direction[2])
        elif data[i] == "v":
            move.append(direction[3])
    return move


def push_box(grid, r, m):
    flag = False
    while flag is False:
        if grid[r[0] + m[0]][r[1] + m[1]] != "#":
            if grid[r[0] + m[0]][r[1] + m[1]] == ".":  # single box pushed into a space
                grid[r[0]][r[1]] = "."
                grid[r[0] + m[0]][r[1] + m[1]] = "O"
                flag = True
            elif grid[r[0] + m[0]][r[1] + m[1]] == "O":
                k, subgrid = 0, []
                s = grid[r[0] + k * m[0]][r[1] + k * m[1]]
                while s != "#":
                    if s == ".":  # multiple boxes are pushed into a space
                        subgrid.pop()
                        for i in range(k - 1):
                            grid[r[0] + (i + 1) * m[0]][
                                r[1] + (i + 1) * m[1]
                            ] = subgrid[i]
                        flag = True
                        break
                    else:
                        s = grid[r[0] + k * m[0]][r[1] + k * m[1]]
                        subgrid.append(s)
                        k += 1
                if (
                    subgrid[-2] == "O" and subgrid[-1] == "#"
                ):  # boxes are pushed into wall
                    r = [r[0] - m[0], r[1] - m[1]]
                    flag = True
                elif (
                    subgrid[-2] == "." and subgrid[-1] == "#"
                ):  # boxes are pushed into a space before wall
                    subgrid.pop(-2)
                    subgrid.insert(0, ".")
                    for i in range(k):
                        grid[r[0] + i * m[0]][r[1] + i * m[1]] = subgrid[i]
                    flag = True
        else:
            r = [r[0] - m[0], r[1] - m[1]]
            flag = True
    return grid, r


data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]
gap_idx = data.index("")
grid = [list(r) for r in data[:gap_idx]]
move = parse_move("".join(data[gap_idx + 1 :]))
nx, ny = len(grid), len(grid[0])

nbox = 0
for j in range(ny):
    for i in range(nx):
        if grid[i][j] == "@":
            r = [i, j]  # position
        elif grid[i][j] == "O":
            nbox += 1

for m in move:
    grid[r[0]][r[1]] = "."
    r = [r[0] + m[0], r[1] + m[1]]
    if grid[r[0]][r[1]] == "#":
        r = [r[0] - m[0], r[1] - m[1]]
    elif grid[r[0]][r[1]] == "O":
        grid, r = push_box(grid, r, m)
    grid[r[0]][r[1]] = "@"

    with open("output.txt", "w") as f:
        f.writelines("".join(line) + "\n" for line in grid)

gps = []
for j in range(ny):
    for i in range(nx):
        if grid[i][j] == "O":
            gps.append([i, j])

result = sum([g[0] * 100 + g[1] for g in gps])
print(result)
