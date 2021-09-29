cont = 0
soma = 0
menor = 0
maior = 0
while True:
    num = input()
    if(num == 'fim'):
            break
    num = int(num)
    if(num<menor or cont ==0):
        menor = num
    if(num>maior or cont ==0):
        maior = num


    cont= cont+1
    soma = soma + int(num)
media = soma/cont
print("{:.2f} {} {}".format(media,maior,menor))

