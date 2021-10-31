quantidade_nomes = int(input())
lista_nomes = []
perigo = 0

for i in range(quantidade_nomes):
    lista_nomes.append(input())

for nome in lista_nomes:
    if nome == 'André':
        perigo = 1

if perigo == 1:
    print('Cuidado!')
else:
    print('Seguro!')
