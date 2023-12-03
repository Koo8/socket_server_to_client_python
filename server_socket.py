import socket

# create a server with socket - use TCP for security, bind to a port and listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP (for UCP : SOCK_DRAM)
s.bind(('127.0.0.1', 12345))
s.listen()

clientSocket, address = s.accept()
print(f'connected to client socket with address {address}' )

# accept connection all the time
while True: 
    # to send message to client
    intmessage = clientSocket.send('the data readableBuffer from server'.encode())
    # to receive message from client
    received_message = clientSocket.recv(1024)
    print(received_message)
    # clientSocket.close()