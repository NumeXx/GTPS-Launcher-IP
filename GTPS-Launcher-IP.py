#!/usr/bin/env python

# Coded By : NumeX
# Rede But Give a Credit :v

import os, sys

ip = input("Enter IP Server : ")
os.system('cls || clear')
print("[Creator] ©NumeX\n[Tools Name] GTPS-Launcher-IP (Python 3.x)\n")
addRed=False
try:
	with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as file:
		if f"{ip} growtopia1.com" in file.read(): 
			print(f"{ip} Already in Host\n")
		else:
			addRed=True;
		file.close()
	if addRed:
		with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as file:
			file.write(f'\r\n{ip} growtopia1.com\n{ip} growtopia2.com')
		print(f"{ip} Was added to Host\n")
		file.close()
except:
	print("Windows hosts failed... Trying linux version (Maybe wine?)\n")
	try:
		with open('\\etc\\hosts', 'r+') as file:
			if f"{ip} growtopia1.com" in file.read():
				print(f"{ip} Already in Host\n")
			else:
				addRed=True;
			file.close()
		if addRed:
			with open('\\etc\\hosts', 'a') as file:
				file.write(f'\n{ip} growtopia1.com\n{ip} growtopia2.com')
			print(f"{ip} Was added to Host\n")
			file.close()
	except:
		print("Unknown error while modifying hosts file??\n?")
		print("Try run application as Administrator/Root or try to add host data manualy.\n")

input("Enter some key to close....")