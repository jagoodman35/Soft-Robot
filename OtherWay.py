# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:32:47 2020

@author: jagoo
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 6000
s.bind((HOST, PORT))

s.listen(5)
print ('Server Started and Listening')
(clientsocket, address) = s.accept()
print ("Connection Found!")
while 1:
    data = clientsocket.recv(1024).decode()
    print (data)
    r='Received'
    clientsocket.send(r.encode())