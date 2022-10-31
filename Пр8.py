#Вариант 1 номер 1
import random
pol = 0
s = 0
p = int(input('Ввод: '))
A = [[random.randrange(10) for i in range(p)] for j in range(p)]
for i in range(p):
    for j in range(i+1, p):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pol += 1
            s += A[i][j]

print('Сумма:', s)
print('Число:', pol)
#Номер 2:
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(B)
#Вариант 3 номер 1
import random
n=int(input('Введите кол-во строк и столбцов матрицы: '))
h=('')
matrix=[[random.randrange(10) for i in range(n)] for j in range(n)]
for elem in matrix:
    print(elem)
for k in range(0,n-1):
    for l in range(k+1,n):
        if matrix[k][l]!=matrix[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Матрица симметрична')
else:
    print('Обычная матрица')
#Номер 2:
print('Случайная матрица: ')
from random import randint
a = [[randint(10, 99) for i in range(9)] for j in range(7)]
for row in a:
    print(*map('{:2d}'.format, row))
print()
print('Преобразованная матрица: ')
max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i
            je = j
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))