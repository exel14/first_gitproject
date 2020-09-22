def registration(username,password,check_password):
    if password == check_password:
        with open('test1.txt', 'a')as reg:
            reg.write(username)
            reg.write(password)
        return ['Вы успешно зарегестрировались',username,password ]
    else:
        return 'Данные введерны неверно!'
username = 'username'
password = 'password'
check_password = 'password'
print(registration(username=username,password=password,check_password=check_password))
def auth(login,passw):
     with open('test1.txt','r')as reg2:
         read_file = reg2.read()
         check_login = read_file[:len(username)]
         check_passw = read_file[len(username):]
         if login == check_login and passw == check_passw:
            return 'Вы успешно авторизовались'
         return 'Вы ввели неверные данные'
print(auth('username','password'))

