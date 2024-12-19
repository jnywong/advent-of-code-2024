def count_concatenations(patterns, target):
    dp = [0] * (len(target) + 1)
    dp[0] = 1

    for i in range(len(target)):
        for pattern in patterns:
            if (
                i + len(pattern) <= len(target)
                and target[i : i + len(pattern)] == pattern
            ):
                dp[i + len(pattern)] += dp[i]

    return dp[len(target)]


data = []
with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

patterns = data[0].split(", ")
desired_patterns = [p for p in data[2:]]

total_concatenations = sum(
    count_concatenations(patterns, dp) for dp in desired_patterns
)
print(f"{total_concatenations}")
