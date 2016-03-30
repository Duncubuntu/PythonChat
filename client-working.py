import socket
import os
import select
import sys

# initial settings
USER = raw_input("USERNAME: ")
PORT_S = raw_input("PORT to connect to: ")
PORT = int(PORT_S)
HOST = raw_input("IP to connect to: ")

def prompt():
   sys.stdout.write(USER + "\n")   
   sys.stdout.flush()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

# attempt connection
s.connect((HOST, PORT))

# successful connection
print 'Connected to remote host. Start sending messages'

while 1:

    socket_list = [sys.stdin, s]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print '\nDisconnected from chat server'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()
        else:
            msg = sys.stdin.readline()
            s.send('\r' + '<' + USER + '>' + msg)
            prompt()