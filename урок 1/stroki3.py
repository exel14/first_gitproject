text = 'football faster'
f = input()
if f in text:
    counter = text.count(f)
    if counter == 1:
        print(text.index(f))
    elif counter>=2:
        print(text.find(f),text.rfind(f))
else:
    print('No letter in string')

