def get_lookup(data, unique, lookup):
    index = unique.index(data)
    l = lookup[index]
    return l


def bubble_sort(arr, unique, reverse_lookup):
    # arr = [int(a) for a in arr]
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            l_rev = get_lookup(arr[i], unique, reverse_lookup)
            if arr[i + 1] in l_rev:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr


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
reverse_lookup = []
for i in range(len(unique)):
    lookup.append([o[1] for o in ordering if unique[i] == o[0]])
    reverse_lookup.append([o[0] for o in ordering if unique[i] == o[1]])

middle = []
for d in data:
    for i in range(len(d) - 1):
        l = get_lookup(d[i + 1], unique, lookup)
        if any(x in l for x in d[: i + 1]):
            d = bubble_sort(d, unique, reverse_lookup)
            flag = True
            break
        else:
            flag = False
    if flag:
        index_mid = int((len(d) - 1) / 2)
        middle.append(int(d[index_mid]))

result = sum(middle)
print(result)
