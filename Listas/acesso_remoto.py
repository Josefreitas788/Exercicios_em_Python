import string
num = int(input())

lista = []
for i in range(num):
    lista.append(input())



print(', '.join(lista[::-1]))
