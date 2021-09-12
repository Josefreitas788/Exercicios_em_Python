segundos = int(input())
horas = segundos//3600
minutos = segundos%3600
segundos = minutos%60
minutos = minutos//60
print("{}h:{}m:{}s".format(horas,minutos,segundos))