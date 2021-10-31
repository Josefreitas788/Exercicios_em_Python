quant_nomes, quant_fatias = input().split()
quant_nomes, quant_fatias = [int(quant_nomes),int(quant_fatias)]

fatias_consumidas = 0
lista_nomes = []
nome_sorteado = 0

for i in range(quant_nomes):
    lista_nomes.append(input().split())
    
    if fatias_consumidas <= quant_fatias-2:
        fatias_consumidas = fatias_consumidas + int(lista_nomes[i][1])

    elif nome_sorteado == 0:
        nome_sorteado = lista_nomes[i][0]


print(nome_sorteado)
