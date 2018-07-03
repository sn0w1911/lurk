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

'''parser = argparse.ArgumentParser(description='Gera endereços pseudoaleatórios de IPs e testa todos.')
parser.add_argument('tentativas', metavar='t', type=int, nargs='+', help='um numero inteiro de tentativas')

args = parser.parse_args()
print args.accumulate(args.tentativas)'''

DECLARE_PATH = 'lurk_dump.txt'


os.system('cls' if os.name == 'nt' else 'clear')
print("***********************************")
print("+++ Lurk 0.3a // We are listening.")
print("+++ Iniciado em " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("***********************************")
print("");

while True:
	ip = ".".join(map(str, (gerador.randint(0, 255)
		for _ in range(4))))
	print(cores.HEADER + cores.WARNING + "[+] " + cores.OKGREEN + "Atualmente testando " + cores.OKBLUE + ip  + cores.OKGREEN + " ↴")
	try:
		socket.gethostbyaddr(ip)
		print(cores.HEADER + cores.WARNING + "     [+] " + cores.OKGREEN + "O IP respondeu.")
		tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tester.settimeout(3)
		test22 = tester.connect_ex((ip, 22))
		if test22 == 0:
			print(cores.HEADER + cores.WARNING + "     [+] " + cores.OKGREEN + "Port 22: aberto.")
		else:
			print(cores.HEADER + cores.WARNING + "     [+] " + cores.FAIL + "Port 22: fechado.")
		testersql = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		testersql.settimeout(3)
		tester3306 = testersql.connect_ex((ip, 3306))
		if tester3306 == 0:
			print(cores.HEADER + cores.WARNING + "     [+] " + cores.OKGREEN + "Port 3306: aberto.")
		else:
			print(cores.HEADER + cores.WARNING + "     [+] " + cores.FAIL + "Port 3306: fechado.")
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
		print(cores.HEADER + cores.WARNING + "     [-] " + cores.FAIL + "O IP não respondeu.")
		print("");
