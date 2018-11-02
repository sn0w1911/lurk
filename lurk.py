#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Esse script é um oferecimento especial Virtual Plaza
Copia não comédia.
cnzn \\ lutz \\ b4con \\ kain \\ loliboyz \\ coolmemes \\ prestushud \\ knet

'''
import random as gerador
import socket
import struct
from time import gmtime, strftime
import os
import argparse

class cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

''' > Classe para segurar as respostas '''
class saida:
	def ipResultado(res):
		if(res >= 0):
			return cores.HEADER + cores.WARNING + "     [+] " + cores.OKGREEN + "O IP respondeu."
		else:
			return cores.HEADER + cores.WARNING + "     [-] " + cores.FAIL + "O IP não respondeu."

DECLARE_PATH = 'lurk_dump.txt'

os.system('cls' if os.name == 'nt' else 'clear')
print("***********************************")
print("+++ Iniciado em " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("***********************************")
print("");

while True:
	ip = ".".join(map(str, (gerador.randint(0, 255)
		for _ in range(4))))
	print(cores.HEADER + cores.WARNING + "[+] " + cores.OKGREEN + "Atualmente testando " + cores.OKBLUE + ip  + cores.OKGREEN + " ↴")
	try:
		socket.gethostbyaddr(ip)
		print(saida.ipResultado(0))
		tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tester.settimeout(3)
		test22 = tester.connect_ex((ip, 22))
		print("")
		if os.path.exists(DECLARE_PATH):
			with open(DECLARE_PATH, 'a') as arq:
				arq.write(ip + '\n')
		else:
			file = open(DECLARE_PATH, 'w+')
			file.close()
			with open(DECLARE_PATH, 'a') as arq:
				arq.write(ip + '\n')

	except socket.herror:
		print(saida.ipResultado(-1))
		print("");
