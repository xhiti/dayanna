matrix = []
action = "!x"
counter = 0
maxRowLength = 0
rowSumList = []
colSumList = []
totalSum = 0

print("Enter the rows elements as integer number and separated by one space!")
print("Press 'x' to stop getting more rows!\n\n")

while action:
    counter += 1
    rowList = []
    givenInput = str(input('Enter row # ' + str(counter) + ':\t'))

    if givenInput == 'x':
        break
    else:
        inputList = givenInput.split()

        for element in inputList:
            isDigit = element.isdigit()

            if isDigit:
                rowList.append(int(element))
            else:
                print("Element given is not a number!")
                break

    if len(rowList) > maxRowLength:
        maxRowLength = len(rowList)

    matrix.append(rowList)


print("\n\nMatrix:\n[")
for i in range(len(matrix)):
    rowSum = 0

    if len(matrix[i]) < maxRowLength:
        numberOfZeros = maxRowLength - len(matrix[i])

        for k in range(numberOfZeros):
            matrix[i].append(0)

    for j in range(maxRowLength):
        rowSum += matrix[i][j]
        totalSum += matrix[i][j]

    rowSumList.append(rowSum)

    print("\t", matrix[i])
print("]")


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        colSum = 0
        for k in range(len(matrix)):
            colSum += matrix[k][j]
        colSumList.append(colSum)
    break


print("SUM of ROWS:\t", rowSumList)
print("SUM of COLS:\t", colSumList)
print("TOTAL SUM:\t\t", totalSum)
