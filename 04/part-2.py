data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append([i for i in line][0])

match = "MAS"
search = [(1, 1), (1, -1)]

count = 0
n = len(data)
for j in range(1, n - 1):
    for i in range(1, n - 1):
        flag = False
        if data[j][i] == "A":
            for dy, dx in search:
                search_1 = data[j + dy][i + dx]
                search_2 = data[j - dy][i - dx]
                word = search_1 + data[j][i] + search_2
                if word == match or word == match[::-1]:
                    flag = True
                else:
                    flag = False
                    break
            count += 1 if flag else 0
