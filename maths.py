import socket

import sys

import time

import errno

import math

from multiprocessing import Process



ok_message = 'HTTP/1.0 200 OK\n\n'

nok_message = 'HTTP/1.0 404 NotFound\n\n'



def process_start(s_sock):

    s_sock.send(str.encode('Welcome to the Server\n'))
    print(s_sock.recv(2048), ' connected!')
    while True:

        data = s_sock.recv(2048)
        data = int(data)

        if data == 1 :

            s_sock.send(str.encode('logarithm function selected\n'))
            number = s_sock.recv(2048)
            number = math.log(int(number))
            s_sock.send(str.encode(str(number)))

        elif data == 2: 

            s_sock.send(str.encode('Square root function selected\n'))
            number = s_sock.recv(2048)
            number = math.sqrt(int(number))
            s_sock.send(str.encode(str(number)))
        elif data == 3: 

            s_sock.send(str.encode('exponential function selected\n'))
            number = s_sock.recv(2048)
            number = math.exp(int(number))
            s_sock.send(str.encode(str(number)))

        else:

            break
        n = s_sock.recv(2048)
        n = int(n)
        if n > 0:
            print(s_sock.recv(2048), 'disconnected!')
            break

    s_sock.close()





if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("",8888))

    print("listening...")

    s.listen(3)

    try:

        while True:

            try:

                s_sock, s_addr = s.accept()

                p = Process(target=process_start, args=(s_sock,))

                p.start()



            except socket.error:



                print('got a socket error')



    except Exception as e:
   		print('an exception occurred!')
   		print(e)
   		sys.exit(1)

    finally:

    	s.close()
