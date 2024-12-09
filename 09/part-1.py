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
    disk.extend(block)

index_free = [sum(disk_map[: 2 * k + 1]) for k in range(n_id)]
n_files = sum([disk_map[i] for i in range(0, n, 2)])
index_free = [
    i for i in index_free if i < n_files
]  # truncate to less than expected n_files

compact = disk.copy()
disk.reverse()
block_free = [disk_map[2 * i + 1] for i in range(n_id - 1)]
i_stop = 0
k = 0
for i in index_free:
    i_start = i_stop
    i_stop = i_start + block_free[k]
    compact[i:i] = disk[i_start:i_stop]
    k += 1

compact = compact[:n_files]
checksum = sum([i * compact[i] for i in range(n_files)])
