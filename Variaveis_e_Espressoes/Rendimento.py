deposito = float(input())
juros = float(input())
juros = deposito*(juros/100)
valor = deposito+juros
print("{:.2f}".format(juros))
print("{:.2f}".format(valor))

