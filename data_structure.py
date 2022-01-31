lst = []
while True:
    data = input('something > ')
    if data == 'stop it':
        break
    else:
        lst.append(data)
    print(lst[:])