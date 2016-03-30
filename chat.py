import socket

def server():
	global port # Available to everything
	host = "localhost" # setsup host machine to run server

	# Create socket object to use for incoming connections
	# and bind to this machine
	comms_socket = socket.socket()
	comms_socket.bind((host, port))

	# status message
	print("Waiting for a chat at ", host, " on port ", port)

	# set socket to listen
	comms_socket.listen(10)
	send_data = ""

	# when there is an incomming connection
	while True:
		# Accept connection. Could add some protection here
		connection, address = comms_socket.accept()
		print("opening chat with ", address)
		# Evaluate input for exit
		while send_data != "EXIT":
			# convert UTF to bytes
			print(connection.recv(4096).decode("UTF-8"))
			send_data = input("Reply: ")
			# encode bytes to UTF for reply and send
			connection.send(bytes(send_data, "UTF-8"))
		send_data = ""
		connection.close()

def client():
	global port
	host = input("Enter the host you want to communicate with." +
		"(Leave blank for localhost): ")

	# evaluate user input and set to localhost if blank
	if host == "":
		host = "localhost"
	# Create socket object
	comms_socket = socket.socket()

	# status message
	print("Start a chat with ", host, " on port ", port)
	comms_socket.connect((host, port)) # make connection
	# while a connection exists
	while True:
		send_data = input("message: ")
		# use socket object to encode bytes to UTF and send
		comms_socket.send(bytes(send_data, "UTF-8"))
		# receieve replies
		print(comms_socket.recv(4096).decode("UTF-8"))

def main():
	# Assign global port a value
	port = int(input("Enter the port you want to communicate over" +
		" (0 for default(50000)): "))

	if port == 0:
		port = 50000
	while True:
		print("Your options are:")
		print("1 - wait for a chat")
		print("2 - initiate a chat")
		print("3 - exit")

		option = int(input("option: "))

		# evaluate choice
		if option == 1:
			server() # If they choose to wait, run server
		elif option == 2:
			client() # If they choose to start, run client
		elif option == 3:
			break # They can exit anytime they want
				  # but they can never leave
		else:
			print("I don't recognize that option")
			main()


# Call main
if __name__ =='__main__':
	main()