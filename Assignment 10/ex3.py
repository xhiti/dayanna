import numpy as np


def create_data(setups: list[dict], seed=None):

    setup = {
        "id": 0,
        "n": 0,
        "a": 0,
        "b": 0
    }

    for setup in setups:
        pass

    return setup


for id_, arr in create_data([
    {"id": "classA", "n": 10, "a": 0, "b": 1.5},
    {"id": "classB", "n": 20, "a": 3, "b": 4},
    {"id": "classC", "n": (5, 10), "a": 0, "b": 10}
], 0).items():
    print("ID and Shape: ", id_, arr.shape)
    print("Array: ", arr)