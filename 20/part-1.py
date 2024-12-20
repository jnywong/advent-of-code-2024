import heapq
import sys

sys.setrecursionlimit(1000)


def dijkstra(data, r, d, max_dist=10000):
    distance = {}
    priority_queue = []
    distance[(r[0], r[1], d)] = 0
    heapq.heappush(priority_queue, (0, r[0], r[1], d))

    dist = 0
    while priority_queue and dist < max_dist:
        (dist, row, col, d) = heapq.heappop(priority_queue)
        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direction.remove(d)  # E W N S
        if distance[(row, col, d)] < dist:
            continue
        for next_dir in direction:
            if (row, col, next_dir) not in distance or distance[
                (row, col, next_dir)
            ] > dist:
                distance[(row, col, next_dir)] = dist
                heapq.heappush(priority_queue, (dist, row, col, next_dir))
        next_row, next_col = row + d[0], col + d[1]
        if (
            0 <= next_row < n
            and 0 <= next_col < n
            and data[next_row][next_col] != "#"
            and (
                (next_row, next_col, d) not in distance
                or distance[(next_row, next_col, d)] > dist + 1
            )
        ):
            distance[(next_row, next_col, d)] = dist + 1
            heapq.heappush(priority_queue, (dist + 1, next_row, next_col, d))
    return distance


data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

n = len(data)
wall = []
for i in range(n):
    for j in range(n):
        if data[i][j] == "S":
            rstart = (i, j)
        elif data[i][j] == "E":
            rend = (i, j)
        elif data[i][j] == "#" and i not in [0, n - 1] and j not in [0, n - 1]:
            wall.append((i, j))


distance = dijkstra(data, rstart, (-1, 0))
distance_no_cheat = min(
    [distance[(rend[0], rend[1], d)] for d in [(0, 1), (-1, 0), (0, -1), (1, 0)]]
)
threshold = 100

grid = data.copy()
distance_cheat = []
k = 1
for w in wall:
    print(f"{k}/{len(wall)}")
    line = list(grid[w[0]])
    line[w[1]] = "."
    grid[w[0]] = "".join(line)
    distance = dijkstra(grid, rstart, (-1, 0), distance_no_cheat - threshold)
    try:
        distance_cheat.append(
            min(
                [
                    distance[(rend[0], rend[1], d)]
                    for d in [(0, 1), (-1, 0), (0, -1), (1, 0)]
                ]
            )
        )
    except KeyError:
        pass
    grid = data.copy()
    k += 1

print(sum([distance_no_cheat - d >= threshold for d in distance_cheat]))
