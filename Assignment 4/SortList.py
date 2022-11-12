# 5. Write a function sort(elements: list, ascending: bool = True) that sorts the specified list
# in-place, i.e., the list is changed directly. The function does not return anything. The parameter
# ascending controls whether the list should be sorted in ascending or in descending order.
def swapListElements(listOfElements, firstIndex, secondIndex):
    listOfElements[firstIndex], listOfElements[secondIndex] = listOfElements[secondIndex], listOfElements[firstIndex]
    return listOfElements


def sort(elements, ascending=True):
    mode = "ASCENDING"
    for i in range(len(elements) - 1):
        isSwaped = False

        for j in range(len(elements) - 1):
            if ascending:
                if elements[j] > elements[j + 1]:
                    swapListElements(elements, j, j + 1)
                    isSwaped = True
            else:
                mode = "DESCENDING"
                if elements[j] < elements[j + 1]:
                    swapListElements(elements, j, j + 1)
                    isSwaped = True

        if not isSwaped:
            break

    print("List Ordered in " + mode + " mode = ", someList)


someList = [1, 3, 0, 4, 5]
print("Execution #1:")
sort(someList)
print("\nExecution #2:")
sort(someList, ascending=False)
