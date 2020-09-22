check_login = input("Авторизуетесь? Да/Нет")
if check_login == 'Да':
    check_user = input("Введите имя пользователя: ")
    check_password = input("Введите пароль: ")
    file1 = open('test.txt')
    check_str = file1.read()
    login = check_str[:8]
    password = check_str[9:]
    if check_user == login and check_password == password:
        print("Вы успешно вошли")
        file1.close()
    else:
        print('Не удается войти.')
else:
    print('До встречи')