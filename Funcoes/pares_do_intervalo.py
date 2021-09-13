def compara(a,b):
    if a==b:
        print("x e igual a y")
        return 0
    if a>b:
        
        print('x e maior que y')
        return 1


    if a<b:
        
        print("x e menor que y")
        return -1


x = int(input())
y = int(input())

num = compara(x,y)


