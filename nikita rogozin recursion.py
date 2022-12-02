# Блок А
n = int(input('N = '))


def recursion(n):
    if (n < 1):
        return n
    else:
        return (n % 10) + (recursion(n // 10))


print(recursion(n))
# Блок Б
n = int(input('N = '))


def Gl(n):
    for i in range(2, n):
        if n % i == 0:
            rez = 'NO'
            break
        else:
            rez = 'YES'
    return (rez)


print(Gl(n))
