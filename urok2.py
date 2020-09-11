num=int(input())
cart_check = ()
original_cart = list(range(1,6))
original_cart_sum = sum(original_cart)
for i in range(1,num):
    new_cart = int(input())
    cart_check.append(new_cart)
search_cart - original_cart_sum - sum(cart_check)
print("Поетрялась карточка под номером:", search_cart)
