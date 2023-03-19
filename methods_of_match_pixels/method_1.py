import numpy as np

# Пробежка по каждому пикселю и просто сравнение цветов предыдущего со следующим.
# Покрасить пиксель в красный цвет если разница цветов больше чувствительности


# a = 7
#
# Не актуально и долго
# def find_diff_colors(arr: np.array, sensitivity: int):
#     for i in range(0, arr.shape[0] - a, a):
#         for j in range(0, arr.shape[1] - a, a):
#             if np.sum(np.abs(arr[i, j + a] - arr[i, j])) > sensitivity:
#                 arr[i, j] = np.array([255, 0, 0], dtype="int16")
#
#     for j in range(0, arr.shape[1] - a, a):
#         for i in range(0, arr.shape[0] - a, a):
#             if np.sum(np.abs(arr[i + a, j] - arr[i, j])) > sensitivity:
#                 arr[i, j] = np.array([255, 0, 0], dtype="int16")
#     return arr.astype("uint8")
#
# Не подходит. при больших значениях step получаются жирные обводки и задублирование объектов
# def find_diff_colors(arr: np.array, sensitivity: int, step: int = 1):
#     """
#     this func finds a difference color between two adjacent pixels with step
#     it means func will search difference between STEP adjacent pixels.
#     Pixels are different when even though 1 out of 3 RGB component more than sensitivity
#     :param arr: image as array with shape (WxHx3)
#     :param step: step between pixels
#     :param sensitivity: it's a difference between pixels which will be compared
#     :return: image as array with red pixels
#     """
#     # create a copy of array
#     fir_arr = arr
#     sec_arr = arr.copy()
#     old_shape = arr.shape
#     # indexes of first and last rows and cols
#     indx_first_row = 0
#     indx_first_col = 0
#     indx_last_row = old_shape[0] - 1
#     indx_last_col = old_shape[1] - 1
#     # delete first and last cols from original arr and copy arr
#     fir_arr_c = np.delete(fir_arr, np.s_[indx_first_col:step], axis=1)
#     sec_arr_c = np.delete(sec_arr, np.s_[indx_last_col - step:indx_last_col], axis=1)
#     # delete first and last rows from original arr and copy arr
#     fir_arr_r = np.delete(fir_arr, np.s_[indx_first_row:step], axis=0)
#     sec_arr_r = np.delete(sec_arr, np.s_[indx_last_row - step:indx_last_row], axis=0)
#     # subtract one array from  other
#     res_by_cols = np.abs(fir_arr_c - sec_arr_c)
#     res_by_rows = np.abs(fir_arr_r - sec_arr_r)
#     # get pixel indexes which contain a number more than sensitivity
#     indxs_cols = np.any(res_by_cols > sensitivity, axis=2)
#     indxs_rows = np.any(res_by_rows > sensitivity, axis=2)
#     # create a false rows and cols
#     false_col = np.zeros([old_shape[0], step], dtype="bool")
#     false_row = np.zeros([step, old_shape[1]], dtype="bool")
#     # add false rows and cols
#     indxs_cols = np.insert(indxs_cols, 0, false_col.T, axis=1)
#     indxs_rows = np.insert(indxs_rows, 0, false_row, axis=0)
#     # create array of all indexes
#     indxs = indxs_cols + indxs_rows
#     # set red color pixels which in indxs
#     fir_arr[indxs] = [255, 0, 0]
#     return fir_arr.astype("uint8")

def step_subtractor(arr1: np.array, arr2: np.array, step: int):
    """

    :param arr1: array
    :param arr2: array
    :param step: step
    :return: result of subtract
    """

    numbers_row = np.arange(arr1.shape[0])
    numbers_col = np.arange(arr1.shape[1])

    indxs_row_in = numbers_row[numbers_row % step == 0]
    indxs_col_in = numbers_col[numbers_col % step == 0]

    indxs_out = np.array(np.meshgrid(indxs_row_in, indxs_col_in)).T.reshape(-1, 2)

    false_array = np.zeros(arr1.shape, dtype="bool")

    false_array[indxs_out[..., 0], indxs_out[..., 1]] = True

    res = np.abs(np.subtract(arr1, arr2, where=false_array, out=arr1))
    return res


def find_diff_colors(arr: np.array, sensitivity: int, step: int = 1):
    """
    this func finds a difference color between two adjacent pixels with step
    it means func will search difference between STEP adjacent pixels.
    Pixels are different when even though 1 out of 3 RGB component more than sensitivity
    :param arr: image as array with shape (WxHx3)
    :param step: step between pixels
    :param sensitivity: it's a difference between pixels which will be compared
    :return: image as array with red pixels
    """
    # create a copy of array
    # делаем копии массивов
    fir_arr = arr
    sec_arr = arr.copy()
    old_shape = arr.shape
    # indexes of first and last rows and cols
    indx_first_row, indx_first_col = 0, 0
    indx_last_row, indx_last_col = old_shape[0] - 1, old_shape[1] - 1
    # delete first and last rows from original arr
    fir_arr_r = np.delete(fir_arr, indx_first_row, axis=0)
    sec_arr_r = np.delete(sec_arr, indx_last_row, axis=0)
    # same
    fir_arr_c = np.delete(fir_arr, indx_first_col, axis=1)
    sec_arr_c = np.delete(sec_arr, indx_last_col, axis=1)
    # subtract one array from  other
    res_by_rows = np.abs(np.subtract(fir_arr_r, sec_arr_r))
    res_by_cols = np.abs(np.subtract(fir_arr_c, sec_arr_c))
    # get pixel indexes which contain a number more than sensitivity
    indxs_rows = np.any(res_by_rows > sensitivity, axis=2)
    indxs_cols = np.any(res_by_cols > sensitivity, axis=2)
    # create a false rows and cols
    false_row = np.zeros([1, old_shape[1]], dtype="int")
    false_col = np.zeros([1, old_shape[0]], dtype="int")
    # add false rows and cols
    indxs_rows = np.insert(indxs_rows, 0, false_row, axis=0)
    indxs_cols = np.insert(indxs_cols, 0, false_col, axis=1)
    # create array of all indexes
    false_indxs = np.zeros((old_shape[0], old_shape[1]), dtype="int")
    indxs = indxs_cols + indxs_rows
    res_indx = step_subtractor(false_indxs, indxs, step).astype("bool")
    # set red color pixels which in indxs
    fir_arr[res_indx] = [255, 0, 0]
    return fir_arr.astype("uint8")
