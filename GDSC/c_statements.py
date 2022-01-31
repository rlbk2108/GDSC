for num in range(1, 101):
    if num % 4 == 0:
        print(num, end=', ')


for num in range(1, 101):
    if num % 7 == 0:
        print(num, end=', ')


for num in range(1, 101):
    if num % 13 == 0 and num % 8 == 0:
        print(num, end=', ')


n = 0
while n <= 100:
    n1 = n * 7 + 23
    if n1 % 2 == 0:
        print(n)
    else:
        print('я обязательно выживу')
    n += 1