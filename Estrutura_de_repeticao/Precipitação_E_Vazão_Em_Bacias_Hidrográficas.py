quant_bacias = int(input())
maior_indice_pluvilometrico = 0
menor_indice_pluvilometrico = 0
menor = 0
maior = 0
areakm2_total = 0
for i in range(quant_bacias):
    #indice pluviometrico
    nome_bacia, areakm2,  verao_ind_pluvi,  outono_ind_pluvi, inverno_ind_pluvi, primavera_ind_pluvi = input().split()
    areakm2,  verao_ind_pluvi,  outono_ind_pluvi, inverno_ind_pluvi, primavera_ind_pluvi = [float(areakm2),float(verao_ind_pluvi),float(outono_ind_pluvi),float(inverno_ind_pluvi),float(primavera_ind_pluvi)]
    
    # encontra o menor indice pluvilometrico
    menor = verao_ind_pluvi
  
    if menor > inverno_ind_pluvi:
        menor = inverno_ind_pluvi
    if menor>outono_ind_pluvi:
        menor = outono_ind_pluvi
    if menor> primavera_ind_pluvi:
        menor = primavera_ind_pluvi
    ## encontra o maiorindice pluvilometrico anual
    maior = verao_ind_pluvi+inverno_ind_pluvi+outono_ind_pluvi+primavera_ind_pluvi

    if  (i==0) or (maior_indice_pluvilometrico< maior):

        maior_indice_pluvilometrico =  maior
        nome_maior_indice_pluvilometrico = nome_bacia

    if (i==0) or (menor_indice_pluvilometrico > menor):

        menor_indice_pluvilometrico =  menor
        nome_menor_indice_pluvilometrico_medio = nome_bacia
    areakm2_total += areakm2
areakm2_total = areakm2_total/quant_bacias
print("{}\n{}\n{:.2f}".format(nome_maior_indice_pluvilometrico,nome_menor_indice_pluvilometrico_medio,areakm2_total))
        