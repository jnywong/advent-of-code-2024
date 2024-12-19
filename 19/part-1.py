import re

data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

patterns = data[0].split(", ")
desired_patterns = [p for p in data[2:]]

arrangements = "(" + "|".join(patterns) + ")*"
pattern = re.compile(arrangements)
print(sum(pattern.fullmatch(dp) is not None for dp in desired_patterns))
