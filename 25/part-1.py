data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

schematic = []
for d in data:
    try:
        schematic.append(data[: data.index("")])
        data = data[data.index("") + 1 :]
    except ValueError:
        schematic.append(data)
        break

m, n = len(schematic[0]), len(schematic[0][0])
key, lock = [], []
[lock.append(s) if s[0] == "#" * 5 else key.append(s) for s in schematic]

key_height, lock_height = [], []

for lck in lock:
    l_t = list(map(list, zip(*lck)))
    height = []
    for pin in l_t:
        idx = pin.index(".")
        height.append(idx - 1)
    lock_height.append(height)

for k in key:
    k_t = list(map(list, zip(*k)))
    height = []
    for pin in k_t:
        idx = pin.index("#")
        height.append(m - idx - 1)
    key_height.append(height)

count = 0
for lck in lock_height:
    for k in key_height:
        fit = [sum(z) for z in zip(lck, k)]
        if any(f > 5 for f in fit):
            continue
        else:
            count += 1

print(count)
