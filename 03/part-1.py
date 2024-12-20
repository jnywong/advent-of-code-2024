import re

with open("input.txt", "r") as file:
    data = file.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", data)

result = sum([int(m[0]) * int(m[1]) for m in matches])
print(f"Result: {result}")
