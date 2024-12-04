data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append([i for i in line][0])

match = "XMAS"
search = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if (dx != 0 or dy != 0)]

count = 0
n = len(data)
for j in range(n):
    for i in range(n):
        for dy, dx in search:
            if all(0 <= j + dy * (k + 1) < n for k in range(len(match) - 1)) and all(
                0 <= i + dx * (k + 1) < n for k in range(len(match) - 1)
            ):
                search_word = [
                    data[j + dy * (k + 1)][i + dx * (k + 1)]
                    for k in range(len(match) - 1)
                ]
                word = data[j][i] + "".join(search_word)
                count += 1 if word == match else 0
