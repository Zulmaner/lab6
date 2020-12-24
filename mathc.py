import socket

import os

ClientSocket = socket.socket()

host = '192.168.73.130'

port = 8888

Id = 'client 1'

os.system('clear')

print('Waiting for connection')

try:

    ClientSocket.connect((host, port))

except socket.error as e:

    print(str(e))



Response = ClientSocket.recv(1024)

print(Response)

ClientSocket.send(str.encode(Id))

Continue = True

while True:

   # while Continue:

        Input = input('1 : logarithm \n2 : square root \n3 : exponential \n\n enter number for selection: ')

        if  0<int(Input)<4:

            ClientSocket.send(str.encode(Input))

            Response = ClientSocket.recv(1024)

            print(Response.decode('utf-8'))

            Input = input('\nEnter number :' )

            ClientSocket.send(str.encode(Input))

            Response = ClientSocket.recv(1024)
            print('answer :',Response.decode('utf-8'))
            print('\n\n\n')
            Input = input('continue? Y/N ').lower()
            if Input == 'n':
               ClientSocket.send(str.encode('1'))
               ClientSocket.send(str.encode(Id))
               break
            else :
               ClientSocket.send(str.encode('0'))
               os.system('clear')

        else :
            print ('invalid option\n\n')


ClientSocket.close()


