import string
frase = input() 
palavras = frase.split()


mensagem = []
for palavra in palavras:
   mensagem.append(palavra[2])

print(''.join(mensagem))
