#Вариант 3 номер 1:
import math
def triangl_1(kat1, kat2):
    kvgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kvgip)
    return gip
def triangl_2(kat1, kat2):
    kvgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kvgip)
    return gip
if triangl_1(5, 7) < triangl_2(9, 11):
    print("Первый больше")
else:
    print("Второй больше")
#Номер 2:
x = ''
a = input('Введите строку: ').lower().split()
for i in range(len(a)):
  a[i] = sorted(a[i])
  x += ''.join(a[i]) + ' '
a = x
print(a)
#Вариант 8 номер 1:
n=int(input('n='))
if n > 0:
    for h in range (1,n + 1):
        p, j = [], h
        while j: p.append(j % 10); j//= 10
        if 0 not in p:
            yes = True
            for b in p:
                if h % b: yes = False; break
            if yes: print(h)
#номер 2:
def func1(a):
    a[0], a[-1] = a[-1], a[0]
    return a
n = int(input('m = '))
a = list(map(int, input('в одну строку через пробел ').split(maxsplit=n)))
print(a)
print(func1(a))

