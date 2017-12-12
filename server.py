import socket

socket1= socket.socket()
host= socket.gethostname()
port= 54321

socket1.bind((host,port))

socket1.listen(20)

while True:
    connection , address = socket1.accept()
    print (' Connection received from : ', address )
    connection.send(' you have been connnected ' )
    connection.close()
