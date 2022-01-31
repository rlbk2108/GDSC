for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=', ')


m = 0
while m <= 100:
    if (m % 3 == 0, 1) and (m % 2 != 0):
        print(m, end=', ')
    m += 1
