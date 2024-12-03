import re

# data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("input.txt", "r") as file:
    data = file.read()

matches = re.findall("mul\((\d+),(\d+)\)", data)

result = sum([int(m[0]) * int(m[1]) for m in matches])
print(f"Result: {result}")
