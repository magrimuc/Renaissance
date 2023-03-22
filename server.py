import socket
import datetime

startpoint = datetime.datetime.now();
while(startpoint  + datetime.timedelta(minutes=1)> datetime.datetime.now()):
    # Initialize Socket Instance
    sock = socket.socket()
    print ("Socket created successfully.")
    # Defining port and host
    port = 8800
    host = 'mgrillo.de'
    # binding to the host and port
    sock.bind((host, port))
    # Accepts up to 10 connections
    sock.listen(10)
    print('Socket is listening...')
    while True:
        # Establish connection with the clients.
        con, addr = sock.accept()
        print('Connected with ', addr)
        # Get data from the client
        #data = con.recv(1024)
        #print(data.decode())
        # joho read
        file = open('sfile.txt', 'wb')
    # joho send to server
        line = con.recv(1024)
    # joho move upwards
        while(line):
            file.write(line)
            line = con.recv(1024)
        file.close()
        print('File has been transferred successfully.')
        con.close()
