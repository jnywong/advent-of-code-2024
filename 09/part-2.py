data = []
with open("input.txt", "r") as file:
    data = file.read()

disk_map = [int(d) for d in data]
n = len(disk_map)
n_id = (n + 1) // 2
arr_id = [j for j in range(n_id)]

disk = []
for i in range(n_id):
    block = [arr_id[i]] * disk_map[2 * i]
    disk.append(block)

# index_free = [sum(disk_map[: 2 * k + 1]) for k in range(n_id)]
# n_files = sum([disk_map[i] for i in range(0, n, 2)])
# index_free = [
#     i for i in index_free if i < n_files
# ]  # truncate to less than expected n_files

block_free = [disk_map[2 * i + 1] for i in range(n_id - 1)]
block_free_copy = block_free.copy()
compact = disk.copy()

for i in range(len(disk) - 1):
    for j in range(len(block_free) - i):
        if len(disk[-(i + 1)]) <= block_free[j]:
            print(disk[-(i + 1)])
            print("fits")
            compact.remove(disk[-(i + 1)])
            compact.insert(j + 1, disk[-(i + 1)])
            block_free[j] = block_free[j] - len(disk[-(i + 1)])
            block_free[-(i + 1)] = block_free[-(i + 1)] + len(disk[-(i + 1)])
            block_free.insert(j, 0)
            break


# compact = [x for xs in compact for x in xs]
# print(compact)
# checksum = sum([int(compact[i])*i for i in range(len(compact)) if compact[i] != '.'])
