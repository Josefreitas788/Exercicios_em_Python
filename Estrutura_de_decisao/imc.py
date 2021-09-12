peso = float(input())
alt = float(input())
imc = peso/(alt*alt)
# PESO NORMAL
p = (alt*alt)*24.9
if imc < 18.5:
    print("{:.2f}\nBaixo peso".format(imc))
elif imc < 24.9:
    print("{:.2f}\nPeso normal".format(imc))
elif imc < 29.9:
    print("{:.2f}\nSobrepeso\n{:.2f}".format(imc,peso-p))
elif imc < 34.9:
    print("{:.2f}\nObesidade grau I\n{:.2f}".format(imc,peso-p))
elif imc < 39.9:
    print("{:.2f}\nObesidade grau II\n{:.2f}".format(imc,peso-p))
else:
    print("{:.2f}\nObesidade grau III\n{:.2f}".format(imc,peso-p))




