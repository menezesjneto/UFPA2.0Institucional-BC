#coding= utf-8
"""

	2019
	by José M.S.M. Neto
		Universidade Federal do Pará 
Este programa faz a captura dos sinais de WiFi que chegam na placa
	de rede.
Se o módulo Cell não estiver instalado, a instalação irá ser feita automaticamente

"""

import os, sys
import subprocess
red, bold, white, yellow, end = '\033[31m', '\033[1m', '\033[37m', '\033[33m', '\033[0;0m' 
try:
	from wifi import Cell
except:
	print("")
	print(white + bold + " [*] Aguarde enquanto uma biblioteca necessária é instalada ..." + end)
	print(white + bold + " [*] Isso pode demorar no máximo três minutos." + end)
	subprocess.check_output("pip3 install wifi", shell=True)
def scanning():
	print("")
	print(yellow + bold + "		Analisador de Redes WiFi" + end)
	print(yellow + bold + "		     by José M.S.M. Neto \n" + end)
	print(white + bold + "A) Analisar o sinal WiFi de todas as redes" + end)
	print(white + bold + "B) Analisar o sinal WiFi apenas de uma rede" + end)
	print("")
	op = input(white + bold + " [*] Digite a sua escolha (A/B): " + end).upper()
	while op != "A" and op != "B":
		op = input(red + bold + " [*] Digite apenas A ou B: " + end).upper()
	if op == "A":
		u = 0
		reg = input(red + bold + " [*] Localização: " + end)
		net = Cell.all("wlan0")
		path = os.getcwd() + "/" + reg + "_all" + ".txt"
		arq = open(path, "w")
		arq.write("		Analisador de WiFi \n")
		arq.write("		Por: José M.S.M. Neto\n")
		arq.write("		Universidade Federal do Pará\n")
		arq.write("---------- Todas as Redes ---------- \n")
		arq.write("	     Localização: " + reg + "\n")
		for networks in net:
			out = "Rede: " + str(u) + "\n"
			out += "    SSID: " + networks.ssid + "\n"
			out += "    Canal: " + str(networks.channel) + "\n"
			out += "    Frequência: " + str(networks.frequency) + "\n"
			out += "    Qualidade: " + str(networks.quality) + "\n"
			out += "    Criptografia: " + str(networks.encrypted) + "\n"
			out += "    Endereço Mac: " + networks.address + "\n"
			out += "    Modo: " + networks.mode + "\n"
			print(out)
			arq.write(out)
			u+=1
		arq.close()
		print(yellow + bold + "Log salvo em: " + end + red + bold + path + end)
		print("")
	else:
		u = 0
		ssid_wifi = input(white + bold + " [*] SSID (nome do WiFi): " + end)
		reg = input(white + bold + " [*] Localização: " + end)
		net = Cell.all("wlan0")
		path = os.getcwd() + "/" + reg + "_" + ssid_wifi + ".txt"
		arq = open(path, "w")
		arq.write("		Analisador de WiFi \n")
		arq.write("		Por: José M.S.M. Neto\n")
		arq.write("		Universidade Federal do Pará\n")
		arq.write("---------- SSID: %s ----------\n" %ssid_wifi)
		arq.write("	   Localização: " + reg + "\n")
		ctrl =  False
		for networks in net:
			if networks.ssid == ssid_wifi:
				out = "Rede: " + str(u) + "\n"
				out += "    SSID: " + networks.ssid + "\n"
				out += "    Canal: " + str(networks.channel) + "\n"
				out += "    Frequência: " + str(networks.frequency) + "\n"
				out += "    Qualidade: " + str(networks.quality) + "\n"
				out += "    Criptografado: " + str(networks.encrypted) + "\n"
				out += "    Endereço Mac: " + networks.address + "\n"
				out += "    Modo: " + networks.mode + "\n"
				print(out)
				arq.write(out)
				u+=1
				ctrl = True
			else:
				pass
		arq.close()
		if ctrl:
			print(yellow + bold + "Log salvo em: " + end + red + bold + path + end)
			print("")
		else:
			print(yellow + bold + "O SSID digitado não foi encontrado!" + end)
			os.remove(path)			

try:	
	scanning()
except (KeyboardInterrupt):
	print("")
	sys.exit(0)	
