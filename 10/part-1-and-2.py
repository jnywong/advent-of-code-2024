data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append([int(i) for i in line[0]])

n = len(data)

pos = [[] for _ in range(10)]
for r in range(n):
    for c in range(n):
        pos[data[r][c]].append((r, c))

peaks_reachable = [[set() for _ in range(n)] for _ in range(n)]
n_trails = [[0 for _ in range(n)] for _ in range(n)]

for height in range(9, 0, -1):
    for r, c in pos[height]:
        if height == 9:
            peaks_reachable[r][c] = {(r, c)}
            n_trails[r][c] = 1
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= rn < n and 0 <= cn < n and data[rn][cn] == height - 1:
                peaks_reachable[rn][cn] |= peaks_reachable[r][c]
                n_trails[rn][cn] += n_trails[r][c]

part1 = sum(len(peaks_reachable[r][c]) for r, c in pos[0])
part2 = sum(n_trails[r][c] for r, c in pos[0])

print(part1)
print(part2)
