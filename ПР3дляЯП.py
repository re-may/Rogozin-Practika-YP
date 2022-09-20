a=int(input('Введите целое число: '))
b=int(input('И ещё одно: '))
c=int(input('и ещё одно пожалуйста: '))
print('Ваши числа в интервале [1,3]: ')
if 1 <= a <= 3:
    print (a)
elif 1 <= b <= 3:
    print (b)
elif 1 <= c <= 3:
    print (c)
else:
    print('Ваши числа не подходят в интервал [1,3]')