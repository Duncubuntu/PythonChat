import socket
import os
import select
import sys

# Initial settings
USER = raw_input("What is your user name?: ")
PORT_S = raw_input("Please enter a port to accept connections: ")
PORT = int(PORT_S)
HOST = raw_input("Please enter an IP to connect too?: ")
RECV_BUFFER = 4096

# Create first prompt
def prompt():
    sys.stdout.write(USER)
    sys.stdout.flush()
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

# Creating socket connection server-side
server_socket.bind((HOST, PORT))
server_socket.listen(10)

input = [server_socket, sys.stdin]
prompt()

print 'Chat Program'

while 1:

    inputready, outputready, exceptready = select.select(input,[],[])

    for sock in inputready:

        if sock == server_socket:
            client, address = server_socket.accept()
            input.append(client)
        elif sock == sys.stdin:
            data = sock.readline()
            for s in input:
                if s not in (server_socket, sys.stdin):
                    s.send(data)    

        else:
            data = sock.recv(RECV_BUFFER)
            if data:
                sys.stdout.write(data)
            else:
                msg = sys.stdin.readline()
                server_socket.send('\r' + '<' + USER + '> ' + msg)
                prompt()
