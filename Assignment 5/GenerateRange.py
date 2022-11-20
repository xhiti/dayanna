# 2. Write a generator function gen_range(start: int, stop: int, step: int = 1) that yields values with range
def gen_range(start, stop, step=1):
    listOfElements = []

    if not isinstance(start, int):
        raise TypeError("START value must be an INTEGER!")

    if not isinstance(stop, int):
        raise TypeError("STOP value must be an INTEGER!")

    if not isinstance(step, int):
        raise TypeError("STEP value must be an INTEGER!")

    if step == 0:
        raise ValueError("STEP value can't be 0!")

    i = start

    if step > 0:
        while i < stop:
            yield i
            i += step
            listOfElements.append(i)

    elif step < 0:
        while i > stop:
            yield i
            i += step
            listOfElements.append(i)

    return listOfElements


print("Example # 1: ", list(gen_range(0, 10)))
print("Example # 2: ", list(gen_range(0, 10, 3)))
print("Example # 3: ", list(gen_range(0, 10, -1)))
print("Example # 4: ", list(gen_range(10, 0)))
print("Example # 5: ", list(gen_range(10, 0, -2)))
print("Example # 6: ", list(gen_range(-10, -3, 2)))
# print("Example # 7: ", list(gen_range(0.0, 10)))
# print("Example # 8: ", list(gen_range(0, 10, 0)))

