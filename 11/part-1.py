data = []
with open("input.txt", "r") as file:
    data = file.read()

data = [d for d in data.split(" ")]
n_blink = 75

for b in range(n_blink):
    print(b)
    i = 0
    while i < len(data):
        if data[i] == "0":
            data[i] = "1"
            i += 1
        elif len(data[i]) % 2 == 0:
            n = len(data[i]) // 2
            data.insert(i, data[i][:n])
            data[i + 1] = str(int(data[i + 1][n:]))
            i += 2
        else:
            data[i] = str(int(data[i]) * 2024)
            i += 1

print(len(data))
