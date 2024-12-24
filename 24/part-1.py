import re
import heapq
import sys

sys.setrecursionlimit(1000)


def evaluate(wire1, wire2, op):
    match op:
        case "AND":
            return 1 if wire1 == 1 and wire2 == 1 else 0
        case "OR":
            return 1 if wire1 == 1 or wire2 == 1 else 0
        case "XOR":
            return 1 if wire1 != wire2 else 0


data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]
gap_idx = data.index("")
initial = dict([(r[0:3], int(r[5])) for r in data[:gap_idx]])

gate = [r for r in data[gap_idx + 1 :]]
connection = []
pattern = r"([a-z0-9]+)\s+([A-Z]+)\s+([a-z0-9]+)\s+->\s+([a-z0-9]+)"
for g in gate:
    wire1, op, wire2, out = re.findall(pattern, g)[0]
    connection.append([wire1, op, wire2, out])

output = dict()
priority_queue = []
for c in connection:
    if c[3].startswith("z"):
        # Add z outputs to priority queue with priority 100
        heapq.heappush(priority_queue, (100, c))

while priority_queue:
    priority, c = heapq.heappop(priority_queue)

    # Check if we can evaluate this connection
    wire1_ready = c[0] in initial or c[0] in output
    wire2_ready = c[2] in initial or c[2] in output

    if wire1_ready and wire2_ready:
        # Get wire values
        wire1_val = initial[c[0]] if c[0] in initial else output[c[0]]
        wire2_val = initial[c[2]] if c[2] in initial else output[c[2]]

        # Evaluate and store result
        output[c[3]] = evaluate(wire1_val, wire2_val, c[1])
        priority += 1
    else:
        # Re-add to queue with increased priority if dependencies not ready
        flag1, flag2 = False, False
        priority -= 1
        for conn in connection:
            if conn[3] == c[0]:
                heapq.heappush(priority_queue, (priority - 1, conn))
                flag1 = True
            elif conn[3] == c[2]:
                heapq.heappush(priority_queue, (priority - 1, conn))
                flag2 = True
            elif flag1 and flag2:
                heapq.heappush(priority_queue, (priority, c))
                break
            heapq.heappush(priority_queue, (priority, c))

z_values = {k: v for k, v in sorted(output.items()) if k.startswith("z")}
binary = "0b"
for val in reversed(z_values.values()):
    binary += str(val)

print(int(binary, 2))
