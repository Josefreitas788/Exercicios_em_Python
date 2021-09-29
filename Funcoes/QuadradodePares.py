def pares_do_intervalo(x):
    if(x>=2):
        if(x%2==0):
                print("{}^2 = {}".format(x,x**2))
    else:
        return 0
    x=x-1
    pares_do_intervalo(x)    
    
num = 1 
while num !=0:

    num = int(input())
    pares_do_intervalo(num)
