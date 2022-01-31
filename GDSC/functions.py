def plus(number, number2):
    return number + number2


def minus(number, number2):
    return number - number2


def multiply(number, number2):
    return number * number2


def divide(number, number2):
    return number / number2


while True:
    somenum = int(input('type the first num or type 0 three times to stop it > '))
    if somenum == 000:
        break
    else:
        somenum2 = int(input('type the second num > '))
        what = input('+ - * / ')
        if what == '+':
            print(plus(somenum, somenum2))
        elif what == '-':
            print(minus(somenum, somenum2))
        elif what == '*':
            print(multiply(somenum, somenum2))
        elif what == '/':
            print(divide(somenum, somenum2))