# 4. Write a function round_ that rounds a given number (integer or float) to ndigits precision:

def round_(number, nDigits=None):
    roundedNumber = number
    strNumber = str(number).split(".")

    if type(number) in (float, int):
        if nDigits is not None:
            digitsBeforeFloat = len(strNumber[0])
            digitsAfterFloat = len(strNumber[1])

            if digitsBeforeFloat == nDigits:
                if digitsAfterFloat == (-1) * nDigits:
                    roundedNumber = number
                else:
                    roundedNumber = number

            elif nDigits > digitsBeforeFloat:
                roundedNumber = number

            elif (-1) * nDigits > digitsBeforeFloat:
                roundedNumber = 0.0

            else:
                multiplier = 10 ** nDigits
                roundedNumber = int((number * multiplier) + (multiplier * 10 ** -nDigits)) / multiplier
        else:
            firstDigit = int(strNumber[0][-1])

            if firstDigit > 4:
                roundedNumber = int(number + 1)
            else:
                roundedNumber = int(number)
    else:
        print("Number given must be integer/float!")
    return roundedNumber


print("Round #1:\t", round_(777.777))
print("Round #2:\t", round_(777.777, 0))
print("Round #3:\t", round_(777.777, 1))
print("Round #4:\t", round_(777.777, 2))
print("Round #5:\t", round_(777.777, 3))
print("Round #6:\t", round_(777.777, 4))
print("Round #7:\t", round_(777.777, -1))
print("Round #8:\t", round_(777.777, -2))
print("Round #9:\t", round_(777.777, -3))
print("Round #10:\t", round_(777.777, -4))
