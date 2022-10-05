print('Задание 1')
a = int(input('Введите целое число: '))
b = int(input('И ещё одно целое число: '))
print('Результат: ')
for i in range(a, b + 1):
    print(i)
print('Задание 2')
a = int(input('Целое число 1: '))
b = int(input('Целое число 2: '))
print('Результат: ')
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print('Результат: ')
        print(i)
print('Задание 3')
a = int(input('Первое целое число: '))
b = int(input('Второе целое число: '))
print('Результат: ')
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
