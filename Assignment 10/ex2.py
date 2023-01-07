import numpy as np


def matrix_stats(matrix: np.ndarray):
    if matrix.ndim != 2:
        raise ValueError("ValueError: The given matrix must be 2D!")

    stats = {
        "total_sum": 0,
        "row_sums": np.array([]),
        "column_sums": np.array([])
    }

    sumOfColumns = []

    for i in range(len(matrix[0])):
        sumOfColumns.append(0)

    currentRow = sumOfColumns
    sumOfAll = 0
    index = 0

    for row in matrix:
        nextRow = row
        sumOfRow = 0

        for element in row:
            sumOfRow += element
            sumOfAll += element

        for i in range(len(currentRow)):
            sumOfColumns[i] = currentRow[i] + nextRow[i]

        index += 1
        currentRow = sumOfColumns
        stats["row_sums"] = np.append(stats["row_sums"], sumOfRow)

    stats["total_sum"] += sumOfAll
    stats["column_sums"] = np.array(sumOfColumns)

    return stats


print("Matrix: \n", np.arange(3 * 4).reshape(3, 4))
print("Matrix Stats #1: ", matrix_stats(np.arange(3 * 4).reshape(3, 4)))