string = input().lower()
sub_str = input().lower()

quant_letras = 0
quant_letras_deixadas = 0
nome = 'john'

for letra in string:
    if letra in nome:
        quant_letras += 1
for letra in sub_str:
    if letra in nome:
        quant_letras_deixadas += 1

print('{} {}'.format(quant_letras-quant_letras_deixadas,quant_letras_deixadas))
