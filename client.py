import socket
import os
import select
import sys

<<<<<<< HEAD
# initial settings
USER = raw_input("USERNAME: ")
PORT_S = raw_input("PORT to connect to: ")
PORT = int(PORT_S)
HOST = raw_input("IP to connect to: ")

def prompt():
   sys.stdout.write(USER + "\n")   
   sys.stdout.flush()

=======
def prompt():
   sys.stdout.write('<You> ')
   sys.stdout.flush()

HOST = '127.0.0.1'
PORT = 9050
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

<<<<<<< HEAD
# attempt connection
s.connect((HOST, PORT))

# successful connection
print 'Connected to remote host. Start sending messages'
=======
s.connect((HOST, PORT))

print 'Connected to remote host. Start sending messages'
prompt()
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64

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
<<<<<<< HEAD
            s.send('\r' + '<' + USER + '>' + msg)
            prompt()
=======
            s.send('\r<Client>: ' + msg)
            prompt()
>>>>>>> dc299a2ddecd966c18f6ca4e98ece4fa45469a64
