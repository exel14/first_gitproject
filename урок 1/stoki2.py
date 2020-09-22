print("Регестрация")
print()
username = input("Введите имя пользователя ")
password = input("Введите пароль ")
check_password = input("Повторите пароль ")
if check_password==password:
    with open('test.txt','a') as file1:
        file1.write(username + '\n')
        file1.write(password)

