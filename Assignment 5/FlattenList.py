# 4. Write a function flatten(nested: list) -> list that flattens an arbitrarily nested list
def flatten(nested):
    if not nested:
        return []
    if isinstance(nested[0], list):
        return flatten(nested[0]) + flatten(nested[1:])
    else:
        return [nested[0]] + flatten(nested[1:])


print("Example # 1:\t", flatten([1, 2, [4, [8, 9, [11, 12], 10], 5], 3, [6, 7]]))
print("Example # 2:\t", flatten([[]]))
print("Example # 3:\t", flatten([[], [], [1], [], [1, [], [4, 5, [[[6]]]], 2, 3]]))
