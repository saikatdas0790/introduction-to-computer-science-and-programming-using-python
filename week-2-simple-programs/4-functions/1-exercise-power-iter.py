def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result


print(iterPower(4, 4))
