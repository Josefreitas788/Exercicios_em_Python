def pares_do_intervalo(x):
    if(x>=2):
        if(x%2==0):
                print(x)
    else:
        return 0
    x=x-1
    pares_do_intervalo(x)    
    
    
num = int(input())
pares_do_intervalo(num)
