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
            ] > dist + 1000:
                distance[(row, col, next_dir)] = dist + 1000
                heapq.heappush(priority_queue, (dist + 1000, row, col, next_dir))
        next_row, next_col = row + d[0], col + d[1]
        if (
            0 <= next_row < nrow
            and 0 <= next_col < ncol
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

nrow, ncol = len(data), len(data[0])
nodes = []
for i in range(nrow):
    for j in range(ncol):
        if data[i][j] == "S":
            rstart = (i, j)
            # nodes.append((i, j))
        elif data[i][j] == "E":
            rend = (i, j)
            # nodes.append((i, j))
        elif data[i][j] == ".":
            nodes.append((i, j))

distance = dijkstra(data, rstart, (0, 1))

print(
    min([distance[(rend[0], rend[1], d)] for d in [(0, 1), (-1, 0), (0, -1), (1, 0)]])
)
