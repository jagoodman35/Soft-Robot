# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:07:12 2020

@author: jagoo
"""

import socket, linecache

HOST = "127.0.0.1"
PORT = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

move_pos = ['0','0','0','0','0']

check = ['0','0','0','0','0']

while True:
    for i in range(len(move_pos)):
      pos = linecache.getline('positions.txt',i+1)
      move_pos[i] = str(pos.strip("\n"))
      linecache.clearcache()
   
    if move_pos != check:
        n = "\n"
        posstr = n.join(move_pos)
        s.send(posstr.encode())
        posstr = ''
        data = ''
        data = s.recv(1024).decode()
        print (data)
        for j in range(len(move_pos)):
            check[j] = move_pos[j]
    
s.close()
