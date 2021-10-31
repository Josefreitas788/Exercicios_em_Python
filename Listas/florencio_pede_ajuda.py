frase = input().split('_')

cont = 0
for nome in frase:
    frase[cont] = nome[:].capitalize()
    cont += 1

print(''.join(frase))


