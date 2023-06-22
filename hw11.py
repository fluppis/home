r = input('Введите "Y" чтобы начать:')
if r == "Y":
    while r == "Y":
        x = int(input('Число1: '))
        y = int(input('Число2: '))
        t = input('введи действие: ')
        if t == '+':
            print(x+y)
        elif t == '-':
            print(x-y)
        elif t == '*':
            print(x*y)
        elif y == 0:
            if y == 0:
                print('Зараз викличу поліцію')
                y = int(input('Спробуй ще раз ввести чісло 2:'))
            if y == 0:
                print('Зі скотиняками не працюю-пока')
            elif y > 0:
                print(x/y)
        elif t == '/':
            print(x / y)
        r = input('Введите "Y" чтобы продолжить:')
    else:
        print("Пока")