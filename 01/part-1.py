import io

list1 = []
list2 = []

with io.open("input.txt", "r") as file:
    for line in file:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

# list1=[3, 4, 2, 1, 3, 3]
# list2= [4, 3, 5, 3, 9, 3]

list1.sort()
list2.sort()

diff = [abs(x - y) for x, y in zip(list1, list2)]

result = sum(diff)

print(result)
