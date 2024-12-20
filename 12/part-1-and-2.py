import skimage
import numpy as np


def encode(letter):
    return ord(letter) - 64


def get_perimeter(region, label):
    perimeter = 0
    for c in region.coords:
        i, j = c
        neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for n in neighbours:
            if (
                not ((0 <= n[0] < label.shape[0]) and (0 <= n[1] < label.shape[1]))
                or region.label != label[n[0]][n[1]]
            ):
                perimeter += 1
    return perimeter


def get_side(region, label):
    side = 0
    for c in region.coords:
        n = label.shape[0]
        i, j = c
        # Exterior corners
        side += (
            1
            if label[i - 1][j] != label[i][j] and label[i][j - 1] != label[i][j]
            else 0
        )
        side += (
            1
            if label[i - 1][j] != label[i][j] and label[i][(j + 1) % n] != label[i][j]
            else 0
        )
        side += (
            1
            if label[(i + 1) % n][j] != label[i][j] and label[i][j - 1] != label[i][j]
            else 0
        )
        side += (
            1
            if label[(i + 1) % n][j] != label[i][j]
            and label[i][(j + 1) % n] != label[i][j]
            else 0
        )
        # Interior corners
        side += (
            1
            if label[i - 1][j] == label[i][j]
            and label[i][j - 1] == label[i][j]
            and label[i][j] != label[i - 1][j - 1]
            else 0
        )
        side += (
            1
            if label[i - 1][j] == label[i][j]
            and label[i][(j + 1) % n] == label[i][j]
            and label[i][j] != label[i - 1][(j + 1) % n]
            else 0
        )
        side += (
            1
            if label[(i + 1) % n][j] == label[i][j]
            and label[i][j - 1] == label[i][j]
            and label[i][j] != label[(i + 1) % n][j - 1]
            else 0
        )
        side += (
            1
            if label[(i + 1) % n][j] == label[i][j]
            and label[i][(j + 1) % n] == label[i][j]
            and label[i][j] != label[(i + 1) % n][(j + 1) % n]
            else 0
        )
    return side


data = []
with open("input.txt") as file:
    for line in file:
        line = line.split()
        data.append([encode(char) for char in line[0]])

arr = np.array(data)
label, n = skimage.measure.label(arr, return_num=True, connectivity=1)
properties = skimage.measure.regionprops(label)
area = [p.area for p in properties]

perimeter = [get_perimeter(p, label) for p in properties]
side = [get_side(p, label) for p in properties]

r1 = sum([a * p for a, p in zip(area, perimeter)])
r2 = sum([a * s for a, s in zip(area, side)])
print(int(r1))
print(int(r2))
