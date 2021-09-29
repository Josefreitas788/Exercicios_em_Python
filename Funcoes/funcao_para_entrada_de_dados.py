def Entrada_dados():
        a = int(input())
        maior = a 
        primeiro = a
        for i in range(9):
            a = int(input())
            if a>maior:
               maior = a
        if (maior%primeiro)!= 0:
            print(maior)
            return 
        else:
            print("{}\n{}".format(maior,primeiro))
Entrada_dados()
    
                
