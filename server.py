import socket
import os
import select
import sys

<<<<<<< HEAD
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
=======
def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

<<<<<<< HEAD
# Creating socket connection server-side
=======
PORT = 9050
HOST = '127.0.0.1'
RECV_BUFFER = 4096

>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
server_socket.bind((HOST, PORT))
server_socket.listen(10)

input = [server_socket, sys.stdin]
<<<<<<< HEAD
prompt()

print 'Chat Program'
=======

print 'Chat Program'
prompt()
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64

while 1:

    inputready, outputready, exceptready = select.select(input,[],[])

    for sock in inputready:

        if sock == server_socket:
            client, address = server_socket.accept()
            input.append(client)
<<<<<<< HEAD
=======
            #data = sock.recv(RECV_BUFFER)
            #if data:
                #sys.stdout.write(data)
        else:
            data = sock.recv(RECV_BUFFER)
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
        elif sock == sys.stdin:
            data = sock.readline()
            for s in input:
                if s not in (server_socket, sys.stdin):
<<<<<<< HEAD
                    s.send(data)    

        else:
            data = sock.recv(RECV_BUFFER)
            if data:
                sys.stdout.write(data)
            else:
                msg = sys.stdin.readline()
                server_socket.send('\r' + '<' + USER + '>' + msg)
                prompt()
=======
                    s.send(data)
            else:
                msg = sys.stdin.readline()
                server_socket.send('\r<Server>: ' + msg)
                prompt()



server_socket.close()
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
