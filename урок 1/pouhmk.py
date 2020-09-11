login=input()
password=input()
password2=input()
if password==password2:
    print("Добро пожаловать")
else:
    print("Пароли не совпадают")
print("Вы действительно хотите войти?")
login1="exel"
password0="1234"
check=input("Да или Нет")
if check=="Да":
    a=input()
    b=input()
    if login1==a and password0==b:
        print("Добро Пожаловать")
else:
    print("До новых встреч")