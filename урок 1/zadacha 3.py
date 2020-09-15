a=int(input())
b=int(input())
i=0
if 1 < a < 10 and 1 < b < 10:
    while a<b:
        a=a*3
        b=b*2
        i=i+1
        print('Текущий год - ',i,'Вес Лимака - ',a,'Вес Боба - ',b)
    print(i)
else:
    print('Неверно')

