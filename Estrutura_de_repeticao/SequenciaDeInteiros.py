num = 1
quantidade = 0
maior = 0
somatorio = 0
media = 0

while True:
     
     num = int(input())
     if num == 0:
         break

     if (quantidade == 0) or (maior< num):
         maior = num
    
     quantidade+=1
     somatorio+=num

if quantidade != 0:
    media = somatorio/(quantidade)

print("{}\n{}\n{:.2f}".format(quantidade,maior,media))