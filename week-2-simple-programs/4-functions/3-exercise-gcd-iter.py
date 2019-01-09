def gcdIter(a, b):
    for num in range(min(a, b), 0, -1):
        if (a % num == 0) and (b % num == 0):
            return num


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))
