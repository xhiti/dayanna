import numpy as np


def create_data(setups: list[dict], seed=None):
    data = dict()
    index = 0

    for setup in setups:
        index += 1
        a = setup["a"]
        b = setup["b"]
        shape = setup["n"]
        randomArray = []

        if type(shape) is int:
            shape = int(shape)

            for i in range(shape):
                if seed and seed > a:
                    randomValue = np.random.uniform(seed, b)
                else:
                    randomValue = np.random.uniform(a, b)

                randomArray.append(randomValue)

        elif type(shape) is tuple:
            for i in range(shape[0]):
                randomRow = []
                for j in range(shape[1]):
                    if seed and seed > shape[0]:
                        randomValue = np.random.uniform(seed, b)
                    else:
                        randomValue = np.random.uniform(a, b)

                    randomRow.append(randomValue)

                randomArray.append(randomRow)

        randomArray = np.array(randomArray, dtype=np.float_)

        data.update({
            setup["id"]: randomArray
        })

    return data


for id_, arr in create_data([
    {"id": "classA", "n": 10, "a": 0, "b": 1.5},
    {"id": "classB", "n": 20, "a": 3, "b": 4},
    {"id": "classC", "n": (5, 10), "a": 0, "b": 10}
], 0).items():
    print("ID and Shape: ", id_, arr.shape)
    print("Array: ", arr)