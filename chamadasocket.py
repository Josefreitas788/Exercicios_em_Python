#!/usr/bin/python
import socket

ip = input('Digite seu ip: ')
port = int(input("Digite o número da porta: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip,port)):
    print("A porta {} está fechada".format(port))
else:
    print("A porta {} está aberta".format(port))