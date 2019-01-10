def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 1:
        if aStr == char:
            return True
        else:
            return False
    else:
        if char == aStr[int(len(aStr)/2)]:
            return True
        elif char < aStr[int(len(aStr)/2)]:
            isIn(char, aStr[:int(len(aStr)/2)])
        else:
            isIn(char, aStr[(int(len(aStr)/2))+1:])


print(isIn("z", "abcd"))
