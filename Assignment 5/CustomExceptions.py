# 5. Consider the following code with custom exceptions ErrorA, ErrorB and ErrorC
def f(x: int):
    try:
        print("ENTERING TRY!")
        g(x)
        print("f1")
    except ErrorA:
        print("f2")
        raise ErrorC
    except ErrorB:
        print("f3")
    else:
        print("f4")
    print("f5")


def g(x: int):
    try:
        h(x)
        print("g1")
    except ErrorA:
        print("g2")
        if x < -10:
            raise ErrorC
        print("g3")
    finally:
        print("g4")


def h(x: int):
    try:
        if x < 0:
            raise ErrorA
        if x > 10:
            raise ErrorB
    finally:
        print("h1")
    print("h2")


print("f(1) => ", f(1))
print("f(-1) => ", f(-1))
print("f(15) => ", f(15))
print("f(-15) => ", f(-15))
