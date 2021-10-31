quant_linhas = int(input())

matriz = []
interrup = 0

for i in range(quant_linhas):
    matriz.append(input().split())

for i in range(quant_linhas-1):
    for j in range(quant_linhas):
        if matriz[i][j] == 'o':
            if matriz[i+1][j] != 'x':
                matriz[i][j] = '.'
                matriz[i+1][j] = 'o'
                interrup = 1
    if interrup == 1:
        break



for i in range(quant_linhas):
    for j in range(quant_linhas):
        print(matriz[i][j],end=' ')
    print()
    
