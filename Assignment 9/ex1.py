import argparse, re


def extract_matr_ids(text: str):
    idNumber = ""
    ids = []

    kLeading = "k(\w+)[0-9]{0,8}"
    idFormat = "id=(\w+)"
    kLeadingIds = re.findall(kLeading, str(text), re.IGNORECASE)
    formatIds = re.findall(idFormat, str(text))

    print("Leading K: ", kLeadingIds)
    print("Id Format: ", formatIds)

    # if len(idNumber) != 8:
    #     if idNumber[0] != 'k' or idNumber[0] != 'K':
    #         re.search(r"([a-z]+[A-Z]+)", idNumber)

    return ids



t = """This is an ID 01234567 this12345678 is not (leading "s"), nei12345678ther
(leading "i" and trailing "t" letters) is 12345678this (trailing "t"). but this
k22222222 is and also this K33333333, but again, k12345678is not valid (trailing
"i") and neither is K123456789 (too many digits) or 1234 (too few digits). Another
valid is ID id=4444 or id=5555555. Invalid examples are id=d1234 (leading "d") or
id=12 (too few digits) or id=x12345678 (leading "x") or id=123456789 (too many
digits) or ID=1234 ("ID" is not equal to "id"). id=11111xyz is valid again."""
print("Output #1: ", extract_matr_ids(t))
