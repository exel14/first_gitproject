def squares():
    import math
    a = []
    b = []
    num = int(input())
    while num != 0:
        a.append(num)
        num = int(input())
    for digit in a:
        result = math.sqrt(digit)
        if (result-int(result)) == 0:
            b.append(result)
    print(a,b)

squares()