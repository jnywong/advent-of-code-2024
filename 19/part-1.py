import re

data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

patterns = data[0].split(", ")
desired_patterns = [p for p in data[2:]]

arrangements = "(" + "|".join(patterns) + ")*"
print(sum(re.fullmatch(arrangements, dp) != None for dp in desired_patterns))
