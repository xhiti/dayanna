# 1. Valid Single Type Function Check
def isValidSingleType(variable, typeRequested):
    if type(variable) is typeRequested:
        return True
    return False


# 2. Valid Multiple Type Function Check
def isValidMultipleType(variable, types):
    if type(variable) in types:
        return True
    return False


# 3. Swap Value of Two Variables
def swapElements(firstElement, secondElement):
    secondElement, firstElement = firstElement, secondElement
    return firstElement, secondElement


# 4. Swap Two Elements in a List
def swapListElements(listOfElements, firstIndex, secondIndex):
    listOfElements[firstIndex], listOfElements[secondIndex] = listOfElements[secondIndex], listOfElements[firstIndex]
    return listOfElements


# 5. Check if a value is Percentage Value
def isPercentageValue(value):
    return isValidSingleType(value, float) and (0.0 < value < 1.0)
