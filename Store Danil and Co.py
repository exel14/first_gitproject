import requests
API_KEY = 'b5253eb5146de956bb2aac5cebf22243-aff2d1b9-e011d560'
API_URL = 'https://api.mailgun.net/v3/sandbox742aca4ebd8545d3b3a7b6e7cb18485f.mailgun.org/messages'

def send_simple_message(final_list,result):
    response = requests.post(
        API_URL,
        auth=("api",API_KEY),
        data={"from": "showmetheway220@gmail.com",
            "to": ["maximneveraa@gmail.com",],
            "subject": "Store Danil and Co",
            "text": [final_list,'Общая сумма: ', result]})
    print(response)
    return response

catalogue = {'microphone':1500,'air-pods':4000,'beats':8000,
             'samsung a5': 10500,'Acer ASPIRE e15': 30000,
             'hard drive':6400,'iphone 8s': 16000,'iphone X': 40000,
             'mouse RX7':8000,'hikvision laland':2280,'kocom': 3990,
             'HIKVISION DS-KD-DIS': 5410, 'commaX cdv':9560,
             'TP-LINK TL-WR841N':1450,'hoco m60': 120,
             'SVEN ap':290,'panasonic': 32460,'Falcon sdd ADATA':6650,
             'Apple Watch':8000}

def login(username,password):
    if len(username) < 20 and not password.isalpha() and not password.isdigit():
        return True
    return False

def counter(money,price):
    if money>price:
        result = money - price
        return result
    else:
        return money


store_list = []
num = 2

def cartage():
    for i in range(2):
        product = input('Введите наименование товара: ')
        store_list.append(product)
    return store_list
cartage()
print(cartage())

final_list = []
for i in store_list:
    final_list.append('Вы купили товар: ' +i)


user_name = 'maksim123'
password = '1234qwer'
user_check = input('Введите имя пользователя: ')
password_check = input('Введите пароль: ')


def buy(store_list):
    if login(username='maksim123',password='1234qwer'):
        global money
        money = 100000
        total_money = money
        for purchase in store_list:
            if purchase in catalogue:
                key_price = catalogue[purchase]
                money = counter(money,key_price)
                result= total_money-money
        send_simple_message(final_list=final_list,result=result)
        return result
    else:
        return 'Зайдите в систему'

print(buy(store_list))

