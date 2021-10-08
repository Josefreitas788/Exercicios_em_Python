frase = input().capitalize()


i = 0

while i < len(frase)-1:
    if frase[i] == '.':
                
        frase = frase[:i+2]  + frase[i+2].swapcase() + frase[i+3:]
    i+=1

print(frase)
