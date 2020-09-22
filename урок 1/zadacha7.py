password = input()
with open('text.txt', 'w') as f2:
    f2.write(password + '\n')
if len(password) > 6:
    print(True)
    with open('text.txt','a') as f2:
        f2.write('True')
else:
    print(False)
    with open('text.txt','a') as f2:
        f2.write('False')