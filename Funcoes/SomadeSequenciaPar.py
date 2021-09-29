def SomadeSequenciaPar(n1,n2,soma):
    if(n2<0):
        print("-1")
        return
    if(n1<=n2-2):
        if(n1%2==0):
            soma= soma+n1          
    else:
        print(soma)
        return soma
    n1=n1+1
    SomadeSequenciaPar(n1,n2,soma)    
    
num = int(input())

SomadeSequenciaPar(0,num,0)
