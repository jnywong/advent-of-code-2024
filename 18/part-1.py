import re
import heapq
import sys

sys.setrecursionlimit(1000)


def dijkstra(data, r, d):
    distance = {}
    priority_queue = []
    distance[(r[0], r[1], d)] = 0
    heapq.heappush(priority_queue, (0, r[0], r[1], d))

    while priority_queue:
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
    data = [re.findall(r"\d+", line.strip()) for line in f]

data = [(int(d[0]), int(d[1])) for d in data]
data = data[:1024]  # first kilobyte

n = 71
grid = [["." for _ in range(n)] for _ in range(n)]

for d in data:
    grid[d[0]][d[1]] = "#"

rstart = (0, 0)
rend = (70, 70)

distance = dijkstra(grid, rstart, (0, 1))
print(
    min([distance[(rend[0], rend[1], d)] for d in [(0, 1), (-1, 0), (0, -1), (1, 0)]])
)
