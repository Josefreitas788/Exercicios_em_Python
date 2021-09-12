import sys
cargo = input()
timetrab = int(input())
salario = float(input())

if salario < 1039:
    print('Salário inválido!')
    sys.exit()

if cargo == 'Gerente':
    if timetrab <= 3:
        print("{:.2f}\n{:.2f}".format(salario*0.12,salario+(salario*0.12)))
    elif timetrab <= 6:
        print("{:.2f}\n{:.2f}".format(salario*0.13,salario+(salario*0.13)))
    else:
        print("{:.2f}\n{:.2f}".format(salario*0.15,salario+(salario*0.15)))

elif cargo == 'Engenheiro':
    if timetrab <= 3:
        print("{:.2f}\n{:.2f}".format(salario*0.07,salario+(salario*0.07)))
    elif timetrab <= 6:
        print("{:.2f}\n{:.2f}".format(salario*0.11,salario+(salario*0.11)))
    else:
        print("{:.2f}\n{:.2f}".format(salario*0.14,salario+(salario*0.14)))
else:
        print("{:.2f}\n{:.2f}".format(salario*0.05,salario+(salario*0.05)))

