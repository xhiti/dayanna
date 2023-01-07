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
            while numberOfMinesLeft != 0:
                mineRowPosition = np.random.randint(0, rows - 1)
                mineColumnPosition = np.random.randint(0, cols - 1)

                if mineField[mineRowPosition][mineColumnPosition] == -1:
                    pass
                else:
                    mineField[mineRowPosition][mineColumnPosition] = -1

                    # 1. Left Neighbour
                    if mineField[mineRowPosition][mineColumnPosition-1] != -1:
                        if mineColumnPosition > 0:
                            mineField[mineRowPosition][mineColumnPosition-1] += 1

                    # 2. Right Neighbour
                    if mineField[mineRowPosition][mineColumnPosition+1] != -1 and mineColumnPosition < cols-1:
                        mineField[mineRowPosition][mineColumnPosition+1] += 1

                    # 3. Up Neighbour
                    if mineField[mineRowPosition-1][mineColumnPosition] != -1 and mineRowPosition > 1:
                        mineField[mineRowPosition-1][mineColumnPosition] += 1

                    # 4. Bottom Neighbour
                    if mineField[mineRowPosition+1][mineColumnPosition] != -1 and mineRowPosition < rows-1:
                        mineField[mineRowPosition+1][mineColumnPosition] += 1

                    # 5. Up-Right Neighbour
                    if mineField[mineRowPosition+1][mineColumnPosition+1] != -1 and mineRowPosition < rows-1 and mineColumnPosition < cols-1:
                        mineField[mineRowPosition+1][mineColumnPosition+1] += 1

                    # 6 Bottom-Left Neighbour
                    if mineField[mineRowPosition-1][mineColumnPosition-1] != -1 and mineRowPosition > 0 and mineColumnPosition > 0:
                        mineField[mineRowPosition-1][mineColumnPosition-1] += 1

                    # 7. Up-Left Neighbour
                    if mineField[mineRowPosition+1][mineColumnPosition-1] != -1 and mineRowPosition < rows-1 and mineColumnPosition > 0:
                        mineField[mineRowPosition+1][mineColumnPosition-1] += 1

                    # 8. Bottom-Right Neighbour
                    if mineField[mineRowPosition-1][mineColumnPosition+1] != -1 and mineRowPosition > 0 and mineColumnPosition < cols-1:
                        mineField[mineRowPosition-1][mineColumnPosition+1] += 1

                    numberOfMinesLeft -= 1

    return np.array(mineField)



print("Output #1: \n", create_minefield(7, 7, 3, 0))
print("\nOutput #2: \n", create_minefield(7, 7, 1, 0))
print("\nOutput #3: \n", create_minefield(7, 7, 20, 0))
print("\nOutput #4: \n", create_minefield(7, 7, 5, 2))