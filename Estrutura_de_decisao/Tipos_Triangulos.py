a = float(input())
b = float(input())
c = float(input())

if(a < b):
    aux = b
    b = a
    a = aux
if(a < c):
    aux = c
    c = a 
    a = aux

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif (a**2==(b**2+c**2)):
    print("TRIANGULO RETANGULO")
elif (a == b ==c):
    print("TRIANGULO EQUILATERO")
elif ((a==b) or (a==c) or (b==c)):
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
