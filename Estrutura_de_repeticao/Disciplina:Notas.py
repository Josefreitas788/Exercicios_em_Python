n = int(input())
contador_aprovados = 0
media_total = 0
for i in range(n):

    nota1,nota2,nota3,faltas = input().split()
    nota1,nota2,nota3,faltas = [float(nota1),float(nota2),float(nota3),int(faltas)]
    
    media = (nota1+nota2+nota3)/3
    media_total += media
    if faltas>16 or  media<=3:
        print("{:.1f} Reprovado".format(media))
    elif  media<5:
        print("{:.1f} Exame".format(media))
    else:
        print("{:.1f} Aprovado".format(media))
        contador_aprovados+=1
print("{:.1f} {}".format(media_total/n,contador_aprovados))
        

        