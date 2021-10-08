frase = input()

con = 'bcdfghjklmnpqrstvwxyz'
for letra in frase:
    if letra.lower() in con:
        
        frase = frase.replace(letra,'p')

print(frase)
    
