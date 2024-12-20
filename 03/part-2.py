import re

# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("input.txt", "r") as file:
    data = file.read() + "do()"

split_do = re.findall(r"do\(\).*?don't\(\)", data, re.DOTALL)
split_do.append(
    re.findall(r".*?don't\(\)", data, re.DOTALL)[0]
)  # edge case: interval before the first don't

matches = []
for s in split_do:
    matches.append(re.findall(r"mul\((\d+),(\d+)\)", s))

result = sum([int(val[0]) * int(val[1]) for match in matches for val in match])
print(result)
