horaIni, minIni, horafim, minfim = input().split()
horaIni, minIni, horafim, minfim = [int(horaIni),int(minIni),int(horafim),int(minfim)]
if(horaIni>=horafim):
    horatotal = (horafim-horaIni)+24
else:
    horatotal = horafim - horaIni
if(minIni>=minfim):
    mintotal = ((minfim - minIni)+60)
    horatotal= horatotal-1
else:
    mintotal = minfim - minIni
if mintotal >= 60:
    mintotal = mintotal-60
    horatotal= horatotal+1
    
print("O jogo durou {} hora(s) e {} minuto(s).".format(horatotal,mintotal))