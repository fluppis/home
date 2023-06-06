x=int(input('Число1: '))
y=int(input('Число2: '))
t=input('введи действие: ')
if t == '+' :
    print(x+y)
elif t == '-' :
    print(x-y)
elif t== '*' :
    print(x*y)
elif y==0  :
    if y==0 :
        print('Зараз викличу поліцію')
        h = int(input('Спробуй ще раз ввести чісло 2:'))
        if h==0:
            print('Зі скотиняками не працюю-пока')
        elif h>0:
            print(x/h)
elif t== '/':
    print(x/y)


