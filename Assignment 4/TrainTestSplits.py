# 3. Write a function create_train_test_splits(data: list, train_size: float) -> tuple that
#    creates two data splits (train and test)
def create_train_test_splits(data, trainSize):
    trainList = []
    testList = []

    if type(trainSize) is float and 0.0 < trainSize < 1.0:
        dataLength = len(data)

        if dataLength > 0:
            trainSplitLength = dataLength * trainSize

            if type(trainSplitLength) is float:
                trainSplitLength = str(trainSplitLength).split(".")
                trainSplitLength = int(trainSplitLength[0])

            for i in range(len(data)):
                if type(data[i]) in (float, int):
                    if i < trainSplitLength:
                        trainList.append(data[i])
                    else:
                        testList.append(data[i])
                else:
                    print("Element '" + str(data[i]) + "' in the data list must be a number (integer/float)!")
                    break

        tupleSplits = (trainList, testList)
        return tupleSplits
    else:
        print("Train size must be a float between 0 and 1!")
        return


print("Train Split List #1: ", create_train_test_splits([], 0.5))
print("Train Split List #2: ", create_train_test_splits(list(range(10)), 0.5))
print("Train Split List #3: ", create_train_test_splits(list(range(10)), 0.67))
print("Train Split List #4: ", create_train_test_splits(list(range(10)), 0.0001))
print("Train Split List #5: ", create_train_test_splits(["a", 1, "test", 29], 0.0001))
