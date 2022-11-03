# 1. Count the number of distinct CAPITAL chars in a string:
givenInput = str(input("Please, enter a word: "))
print("Given word: ", givenInput)

counter = 0

if givenInput == '':
    print("No given word detected!")
    pass
else:
    # remove the duplicated CAPITAL chars in the given string:
    string = ""
    for char in givenInput:
        if char.isupper() and char in string:
            pass
        else:
            string += char

    print("Given word after removing duplicates: ", string)

    # now count the number of CAPITAL chars at the new string:
    for char in string:
        if char.isupper():
            counter += 1

print("Number of CAPITAL chars is: ", counter)
