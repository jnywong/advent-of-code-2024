import re

data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line)

position = []
velocity = []

for i in range(len(data)):
    p = re.findall(r"-?\d+", data[i][0])
    v = re.findall(r"-?\d+", data[i][1])
    position.append([int(p[0]), int(p[1])])
    velocity.append([int(v[0]), int(v[1])])

nx, ny = 7, 11
for t in range(100):
    for i in range(len(position)):
        position[i][0] += velocity[i][0]
        position[i][1] += velocity[i][1]
        position[i][0] %= nx
        position[i][1] %= ny

    a = [[" " for _ in range(ny)] for _ in range(nx)]
    for p in position:
        a[p[0]][p[1]] = "#"
    # input(f"t={t}: Press Enter to continue...")

    with open("output.txt", "w") as file:
        file.writelines("\n".join("".join(r) for r in a))
