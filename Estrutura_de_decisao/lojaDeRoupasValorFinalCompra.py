valor, parcela = input().split()
valor, parcela = [float(valor),float(parcela)]
if parcela == 1:
    parcelas=(valor-(valor*0.05))/parcela
    print("{:.2f} {:.2f}".format(valor-(valor*0.05),parcelas))
elif parcela == 2:
    print("{:.2f} {:.2f}".format(valor,valor/parcela))
elif parcela == 3:
    parcelas = (valor+(valor*0.05))/parcela
    print("{:.2f} {:.2f}".format(valor+(valor*0.05),parcelas))
elif parcela == 4:
    parcelas = (valor+(valor*0.1))/parcela
    print("{:.2f} {:.2f}".format(valor+(valor*0.1),parcelas))
