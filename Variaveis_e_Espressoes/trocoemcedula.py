valor1 = int(input())
nota100 = valor1//100
valor = valor1%100
nota50 = valor//50
valor = valor%50
nota20 = valor//20
valor = valor%20
nota10 = valor//10
valor = valor%10
nota5 = valor//5
valor = valor%5
nota2 = valor//2
valor = valor%2
nota1 = valor//1
print(valor1)
print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(nota100,nota50,nota20,nota10,nota5,nota2,nota1))
