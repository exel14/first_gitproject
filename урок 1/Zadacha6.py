text = 'hello world its python programmist i am new here'
space = text.index(' ')
with open('test.txt','a')as f1:
    f1.write(text[:space] + '\n')
print(text[:space])

