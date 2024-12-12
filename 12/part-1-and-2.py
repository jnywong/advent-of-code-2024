import skimage
import numpy as np


def encode(letter):
    return ord(letter) - 64


def get_perimeter(region, label):
    perimeter = 0
    for t in region.coords:
        i, j = t
        neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for n in neighbours:
            if (
                not ((0 <= n[0] < label.shape[0]) and (0 <= n[1] < label.shape[1]))
                or region.label != label[n[0]][n[1]]
            ):
                perimeter += 1
    return perimeter


data = []
with open("input.txt") as file:
    for line in file:
        line = line.split()
        data.append([encode(l) for l in line[0]])

arr = np.array(data)
label, n = skimage.measure.label(arr, return_num=True, connectivity=1)
properties = skimage.measure.regionprops(label)
area = [p.area for p in properties]

perimeter = [get_perimeter(p, label) for p in properties]
result = sum([a * p for a, p in zip(area, perimeter)])
print(int(result))
