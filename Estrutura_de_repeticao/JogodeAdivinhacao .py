#numero a ser advinhado
num = int(input("Digite o número a ser adivinhado: "))
verificador = True
while(verificador):
    chute = int(input("Chute um número inteiro: "))
    if num == chute:
        print("Parabéns! Você acertou.")
        verificador = False
    elif chute< num:
        print("O número correto é maior. ")
    else:
        print("O número correto é menor. ")

