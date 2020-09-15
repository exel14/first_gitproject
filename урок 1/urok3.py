a = [1,2,3,4,5,6,7,8]
i = 0
j = 0
second = 0
while i < len(a):
    if second != a[i]:
        second = a[i]
        j = j + 1
    i = i + 1
print (j, len(a))