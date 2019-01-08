def recurPower(base, exp):
    if exp <= 1:
        return base
    return base * recurPower(base, exp-1)


print(recurPower(4, 4))
