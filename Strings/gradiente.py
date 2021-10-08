frase = input()

maiuscula = 'ABCDEFGHIJKLMNOPKRSTUVWXYZ'
minuscula = 'abcdefghijklmnopkrstuvwxyz'
espaco = ' '
numero = '1234567890'
txt = []


for letra in frase:
    if letra in maiuscula:
        txt.append('U')
    if letra in minuscula:
        txt.append('L')
    if letra in espaco:
        txt.append('W')
    if letra in numero:
        txt.append('D')

print(''.join(txt))
