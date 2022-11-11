# 1. Write a function FIB that calculates and returns the n-th Fibonacci number using for loop:
def fib(n):
    if n < 0:
        return -1

    if 0 >= n <= 1:
        return 1

    previousNumber = 0
    currentNumber = 1

    for i in range(n - 1):
        newNumber = previousNumber + currentNumber
        previousNumber = currentNumber
        currentNumber = newNumber

    return currentNumber


givenInput = str(input("Please enter a number: "))

if givenInput.strip("-").isdigit():
    fibonacciNumber = fib(int(givenInput))
    print("fib(" + str(givenInput) + ") = " + str(fibonacciNumber))
else:
    print("INVALID '" + str(givenInput) + "' given, input must be an INTEGER!")
