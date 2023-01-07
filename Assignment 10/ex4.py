import numpy as np


def create_minefield(rows: int, cols: int, n_mines: int, seed=None):
    if rows < 2:
        raise ValueError("ValueError: Number of rows must be greater or equal than 2!")

    if cols < 2:
        raise ValueError("ValueError: Number of columns must be greater or equal than 2!")

    if n_mines < 1 or n_mines >= rows * cols:
        raise ValueError("ValueError: Number of mines isn't allowed!")

    mineField = []
    mineRowPosition = 0
    mineColumnPosition = 0
    numberOfMinesLeft = n_mines

    # 1. Create Field
    for i in range(rows):
        randomRow = []

        for j in range(cols):
            randomValue = int(np.random.default_rng(seed).random())
            randomRow.append(randomValue)

        mineField.append(randomRow)

    # 2. Set Mines
    for i in range(len(mineField)):
        for j in range(len(mineField[0])):
            print("Value: ", mineField[i][j])

            while numberOfMinesLeft != 0:
                mineRowPosition = np.random.randint(0, rows - 1)
                mineColumnPosition = np.random.randint(0, cols - 1)

                if i == mineRowPosition and j == mineColumnPosition:
                    pass
                else:
                    mineField[i][j] = -1
                    numberOfMinesLeft -= 1

    return np.array(mineField)



print("\n\nOutput #1: \n", create_minefield(7, 7, 3, 0))