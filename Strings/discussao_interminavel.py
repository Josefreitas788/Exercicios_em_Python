qtd_de_linhas = int(input())
quant_p = 0
quant_u = 0

for i in range(qtd_de_linhas):
    j=0 
    frase = input().lower()
    while j < len(frase):
        if frase[j] == 'p':
            quant_p += 1
        
        if frase[j] == 'u':
            quant_u += 1
        j+=1
print("{} {}".format(quant_p,quant_u))

