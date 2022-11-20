# 1. Write a function that calculates and returns the n-th Fibonacci number using recursion.
def fib(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


givenInput = str(input("Please enter a number: "))

if givenInput.strip("-").isdigit():
    fibonacciNumber = fib(int(givenInput) + 1)
    print("fib(" + str(givenInput) + ") = " + str(fibonacciNumber))
else:
    print("INVALID '" + str(givenInput) + "' given, input must be an INTEGER!")
