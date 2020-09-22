def Prime(x):
    i = 2
    while x % i != 0:
        i = i + 1
    if x == i:
        return True
    return False

print(Prime(7))