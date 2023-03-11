import numpy as np


# Пробежка по каждому пикселю и просто сравнение цветов предыдущего со следующим.
# Покрасить пиксель в красный цвет если разница цветов больше чувствительности

def find_diff_colors(arr: np.array, sensitivity: int):
    for i in range(0, arr.shape[0] - 7, 7):
        for j in range(0, arr.shape[1] - 7, 7):
            if np.sum(np.abs(arr[i, j + 7] - arr[i, j])) > sensitivity:
                arr[i, j] = np.array([255, 0, 0], dtype="int16")

    for j in range(0, arr.shape[1] - 7, 7):
        for i in range(0, arr.shape[0] - 7, 7):
            if np.sum(np.abs(arr[i + 7, j] - arr[i, j])) > sensitivity:
                arr[i, j] = np.array([255, 0, 0], dtype="int16")
    return arr.astype("uint8")
