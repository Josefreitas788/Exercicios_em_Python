mesa1 = 4
mesa2 = 2
mesa3 = 8
sem_mesa = 0
mesa1ocup = 0
mesa2ocup = 0
mesa3ocup = 0

while True:
    num_pessoas = input()
    if num_pessoas == 'Fim':
        break
    num_pessoas = int(num_pessoas)
    if num_pessoas <= mesa2:
        mesa2ocup = num_pessoas
        mesa2 = -100
    elif num_pessoas <= mesa1:
        mesa1ocup = num_pessoas
        mesa1 = -100
    elif num_pessoas <= mesa3:
        mesa3ocup = num_pessoas
        mesa3 = -100
    else:
        sem_mesa = sem_mesa + num_pessoas

print("{} {} {} {}".format(mesa1ocup,mesa2ocup,mesa3ocup,sem_mesa))
    
