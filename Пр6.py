print('1: ')
x = 0
from random import *
lst = [randint(0,50) for i in range(15)]
print('Список lst: ', lst)
if (lambda x : lst.count(x) > 1):
    print(*filter(lambda x: lst.count(x) > 1, lst))
else:
    print('Повторяющихся чисел нет.')
print('2: ')
import random
arr, arr2 = [], []
for i in range(15):
    arr.append(random.randrange(0, 50))
    arr2.append(arr[i])
    if arr[i] < 10:
        arr2[i] = 0
    if arr[i] > 20:
        arr2[i] = 1
print("Исходный:\n", str(arr), "\nПреобразованный:\n", str(arr2))
input()
