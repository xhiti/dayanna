# 2. Write a function CLIP that returns a list of clipped values based on arbitrary many input values:

def clip(*values, min_=0, max_=1):
    clippedList = []

    if len(values) == 0:
        return clippedList

    if not type(min_) in (float, int):
        print("MIN value must be a number (integer/float)!")
        return clippedList

    if not type(max_) in (float, int):
        print("MAX value must be a number (integer/float)!")
        return clippedList

    for value in values:
        if type(value) in (float, int):
            if value < min_:
                clippedList.append(min_)
            elif value > max_:
                clippedList.append(max_)
            else:
                clippedList.append(value)
        else:
            print("Value '" + str(value) + "' is not a number (integer/float)!")
            break

    return clippedList


print("Clipped List #1: ", clip())
print("Clipped List #2: ", clip(1, 2, 0.1, 0))
print("Clipped List #3: ", clip(-1, 0.5))
print("Clipped List #4: ", clip(-1, 0.5, min_=-2))
print("Clipped List #5: ", clip(-1, 0.5, max_=0.3))
print("Clipped List #6: ", clip(-1, 0.5, min_=2, max_=3))
print("Clipped List #7: ", clip(-1, 0.5, min_="asdas", max_="a0000sdas"))
print("Clipped List #8: ", clip("sad", "sadas", min_=1, max_=2))

