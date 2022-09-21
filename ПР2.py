import math
x=float(input('Введите переменную x: '))
y=float(input('Введите переменную y: '))
z=float(input('Введите переменную z: '))
s = (math.pow(2,-x)) * (math.sqrt((x+(abs(y))**(1./4.)))) * ((math.pow((math.e),x-1/math.sin(z)))**(1./3.))
print(s)
