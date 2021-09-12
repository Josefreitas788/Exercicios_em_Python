n = int(input())
soma = 0
soma_maior = 0
soma_menor = 0
for i in range(n):
    x,y = input().split()
    x,y = [int(x),int(y)]
    j=x
    cont = 0
    while cont < y :

        if j%2 != 0:

            soma+=j
            cont+=1
        j+=1
    print(soma)

    if (i==0) or (soma<soma_menor):
        soma_menor = soma
    if (i==0) or (soma>soma_maior):
        soma_maior = soma

    soma=0
print(soma_maior)
print(soma_menor)
print("{:.2f}".format((soma_maior+soma_menor)/2))

        

    