#Блок A, номер 4
n = float(input('N = '))
def recursion(n):
    if (n < 10):
            return n
    else: 
            return (n % 10) + (recursion(n / 10))
print(recursion(n))
#Блок Б, номер 4
n=int(input('N = '))
def Gl(n):
    for i in range (2, n):
        if n%i==0:
            rez='NO'
            break
        else:
            rez='YES'
    return(rez)
print(Gl(n))
