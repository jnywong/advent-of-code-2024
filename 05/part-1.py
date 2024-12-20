data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.split()
        data.append(line)

index_sep = data.index([])
ordering = [d[0].split("|") for d in data[:index_sep]]
data = [d[0].split(",") for d in data[index_sep + 1 :]]

unique = list(set([o for order in ordering for o in order]))
lookup = []
for i in range(len(unique)):
    lookup.append([o[1] for o in ordering if unique[i] == o[0]])

middle = []
for d in data:
    for i in range(len(d) - 1):
        index = unique.index(d[i + 1])
        var = lookup[index]
        if any(x in var for x in d[: i + 1]):
            flag = False
            break
        else:
            flag = True
    if flag:
        index_mid = int((len(d) - 1) / 2)
        middle.append(int(d[index_mid]))

result = sum(middle)
print(result)
