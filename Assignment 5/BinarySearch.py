# 3. Write a function binary_search(elements: list, x) -> bool that applies a binary search on the
#    list elements while searching for the value x
def binary_search(elements, x):
    if not type(x) is int:
        return False

    if len(elements) == 0:
        return False

    middleIndex = len(elements) // 2

    if elements[middleIndex] == x:
        return True
    else:
        if x < elements[middleIndex]:
            return binary_search(elements[:middleIndex], x)
        else:
            return binary_search(elements[middleIndex + 1:], x)


my_sorted_list = [1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
print("Example # 1:\t", binary_search(my_sorted_list, 1))
print("Example # 2:\t", binary_search(my_sorted_list, 20))
print("Example # 3:\t", binary_search(my_sorted_list, 21))
print("Example # 4:\t", binary_search(my_sorted_list, "hello"))
