import os



class Reader:
    def __init__(self, path:str):
        if len(path) == 0:
            raise ValueError("ValueError: The given path doesn't represent a file!")
        else:
            self.path = path

    def close(self):
        self.close()

    def __len__(self):

        # Method 1:
        numberOfBytes = os.path.getsize(self.path)
        # print("Number Of Bytes Method 1: ", numberOfBytes)

        # Method 2:
        # numberOfBytes = file.seek(0, os.SEEK_END)
        # print("Number Of Bytes 2: ", numberOfBytes)

        return numberOfBytes

    def __getitem__(self, key):
        if type(key) is int:
            numberOfBytes = Reader.__len__(self)

            if key in range(-numberOfBytes, numberOfBytes):
                file = open(self.path, "rb")
                index = 0
                lineNumber = 1

                for line in file:
                    line = str(line)[2:-1].strip()
                    print("LINE " + str(lineNumber) + ": ", line)

                    lineNumber += 1
                    for char in line:
                        print("CHAR: ", char)
                        if key < 0:
                            key = numberOfBytes + key
                        if key == index:
                            # character = file.seek(char, os.SEEK_CUR)
                            # print("CHARACTER: ", character)
                            return char
                        index += 1
                print("INDEX: ", index)
                # index = 0
                # if key < 0:
                #     key = numberOfChars + key
                #     print("KEY: ", key)
                # for line in file:
                #     print("Line: ", line)
                #     charLines = str(line).split("b'")
                #     charLines = charLines[1].split("\\r\\n")[0]
                #     charLines = charLines.split("'")[0]
                #     for char in charLines:
                #         if index == key:
                #             return char
                #         index += 1
            else:
                raise IndexError("IndexError: Reader index out of range!")
        else:
            raise TypeError("TypeError: indexing expects 'int', not 'str'!")


r = Reader("ex2_data.txt")
print("Character with index = 0: ", r[0])
print("Character with index = 1: ", r[1])
print("Character with index = -1: ", r[-1])
try:
    r["hi"]
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
try:
    r[100]
except IndexError as e:
    print(f"{type(e).__name__}: {e}")


