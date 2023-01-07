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
        # Reader.close(self)
        # print("Number Of Bytes Method 1: ", numberOfBytes)

        # Method 2:
        # numberOfBytes = file.seek(0, os.SEEK_END)
        # Reader.close(self)
        # print("Number Of Bytes 2: ", numberOfBytes)

        return numberOfBytes

    def __getitem__(self, key):
        if type(key) is int:
            numberOfBytes = Reader.__len__(self)

            if key in range(-numberOfBytes, numberOfBytes):
                file = open(self.path, "rb")

                if key < 0:
                    key = numberOfBytes + key

                file.seek(key, os.SEEK_CUR)
                currentCharacter = file.read()

                return  currentCharacter

            else:
                raise IndexError("IndexError: Reader index out of range!")
        else:
            raise TypeError("TypeError: indexing expects 'int', not 'str'!")


r = Reader("ex2_data.txt")
print("Output #1:", r[0])
print("Output #2:", r[1])
print("Output #3:", r[-1])
try:
    r["hi"]
except TypeError as e:
    print(f"Output #4: {type(e).__name__}: {e}")
try:
    r[100]
except IndexError as e:
    print(f"Output #5: {type(e).__name__}: {e}")


