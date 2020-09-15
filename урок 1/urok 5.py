a = [1,2,3]
b = [3,4,5]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)