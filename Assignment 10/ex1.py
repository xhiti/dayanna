import numpy as np


def extend(arr: np.ndarray, size: int, fill=None):
    newArr = arr
    arrSum = 0
    arrMean = 1

    if arr.ndim > 1:
        raise ValueError("ValueError: The given array must be 1D!")

    if size < len(arr):
        raise ValueError("ValueError: The size can't be smaller than the 1D array!")

    if size == len(arr):
        return newArr

    addElements = size - len(arr)

    if np.issubdtype(arr.dtype, np.number):
        for elements in arr:
            arrSum += elements
        arrMean = arrSum / len(arr)

    if fill is None:
        for i in range(addElements):
            newArr = np.append(newArr, 1)
    else:
        if fill == "mean":
            if np.issubdtype(arr.dtype, np.int_):
                for i in range(addElements):
                    newArr = np.append(newArr, int(arrMean))
            elif np.issubdtype(arr.dtype, np.float_):
                for i in range(addElements):
                    newArr = np.append(newArr, float(arrMean))
            elif np.issubdtype(arr.dtype, np.str_):
                for i in range(addElements):
                    newArr = np.append(newArr, "mean")
        else:
            for i in range(addElements):
                newArr = np.append(newArr, fill)

    return newArr


print("Extend #1: ", extend(np.arange(4), 7))
print("Extend #2: ", extend(np.arange(4), 7, fill=0))
print("Extend #3: ", extend(np.arange(4), 7, fill="mean"))
print("Extend #4: ", extend(np.arange(4, dtype=float), 7, fill="mean"))
print("Extend #5: ", extend(np.array(["hello", "world"]), 5, "mean"))
