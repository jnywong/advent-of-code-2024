import io

list1=[]
list2=[]

with io.open("input.txt", "r") as file:
    for line in file:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

# list1=[3, 4, 2, 1, 3, 3]
# list2= [4, 3, 5, 3, 9, 3]

count=[]
for x in list1:
    i=0
    for y in list2:
        if y == x:
            i+=1
    count.append(i)

similarity = [a*b for a, b in zip(list1, count)]
print(sum(similarity))