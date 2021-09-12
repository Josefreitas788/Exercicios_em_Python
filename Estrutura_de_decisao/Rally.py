sectrecho1, veloctrecho1, sectrecho2, veloctrecho2 = input().split()
sectrecho1, veloctrecho1, sectrecho2, veloctrecho2 = [int(sectrecho1), int(veloctrecho1), int(sectrecho2), int(veloctrecho2)]

# TRECHO 1
if sectrecho1<1800:
    sectrecho1 = 2*(1800-sectrecho1)*-1
else:
    sectrecho1 = 1*(sectrecho1 - 1800)*-1
if veloctrecho1>60:
    veloctrecho1 = (10*(veloctrecho1-60))*-1
    pontecho1 = veloctrecho1+sectrecho1
else:
    pontecho1 = sectrecho1

# TRECHO 2
if sectrecho2<3600:
    sectrecho2 = 2*(3600-sectrecho2)*-1
else:
    sectrecho2 = 1*(sectrecho2 - 3600)*-1
if veloctrecho2>40:
    veloctrecho2 = 20*(veloctrecho2-40)*-1
    pontecho2 = veloctrecho2+sectrecho2
else:
    pontecho2 = sectrecho2
print("{}\n{}\n{}\n{}\n{}\n{}".format(sectrecho1, pontecho1, sectrecho2, pontecho2,sectrecho1+sectrecho2,pontecho2+pontecho1))