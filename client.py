import socket

socket1= socket.socket()
host= socket.gethostname()
port= 54321

socket1.connect((host,port))

print( socket1.recv(1024))

socket1.close()
