# 1. Write a function FIB that calculates and returns the n-th Fibonacci number using for loop:
def fib(n):
    if n < 0:
        return -1

    if 0 >= n <= 1:
        return n

    previousNumber = 0
    currentNumber = 1

    for i in range(n - 1):
        nextNumber = previousNumber + currentNumber
        previousNumber = currentNumber
        currentNumber = nextNumber

    return currentNumber


givenInput = str(input("Please enter a number: "))

if givenInput.strip("-").isdigit():
    fibonacciNumber = fib(int(givenInput))
    print("fib(" + str(givenInput) + ") = " + str(fibonacciNumber))
else:
    print("INVALID '" + str(givenInput) + "' given, input must be an INTEGER!")

# print("fib(0) = \t", fib(0))
# print("fib(1) = \t", fib(1))
# print("fib(2) = \t", fib(2))
# print("fib(3) = \t", fib(3))
# print("fib(4) = \t", fib(4))
# print("fib(5) = \t", fib(5))
# print("fib(6) = \t", fib(6))
# print("fib(7) = \t", fib(7))
# print("fib(8) = \t", fib(8))
# print("fib(9) = \t", fib(9))
# print("fib(10) = \t", fib(10))
