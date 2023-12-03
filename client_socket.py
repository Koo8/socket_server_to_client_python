import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))
# client receiving message
msg =s.recv(1024).decode()
print(msg)
# client sending message
while True:
    user_msg = input(': ')
    s.send(user_msg.encode())



