import socket
import pickle
#import sys
from _thread import *
from player import Player


#takes ipv4, 8.8.8.8
#local ip ethernet
server = "10.0.0.132" #127.0.0.1 #10.0.0.132
port = 5555 #80, 443, 5555 is usually an open port

#socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE) for IPv4.
#socket(AF_INET6, SOCK_DGRAM, IPPROTO_UDPLITE) for IPv6.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    # we need to bind the server with the port
    s.bind((server,port)) 
except socket.error as e:
    #if it doesn't work then we will know
    str(e)

s.listen(2)#blank will allow for unlimited connections
print("Waiting for a connection, Server Started")
players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,0,255))]


"""def (str):#want a (45,423)
    str = str.split(",")
    return int(str[0]), int(str[1])


def (tup):
    return str(tup[0]) + "," + str(tup[1])"""


"""pos = [(0,0),(100,100)]#holds positions of players"""


def threaded_client(conn,player):#connection
    #conn is our socket
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))#if error: inc size returns bites from deata received   
            players[player] = data
        
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                    
                print("Received: ", data)
                print("Sending: ", reply)
                
            conn.sendall(pickle.dumps(reply))#socket.sendall(bytes[, flags])
        except:
            break
    
    print("Lost connection")
    conn.close()

#threading: a process running in the background. 
#Calls a function but doesn't need that function to finish yet
#Multiple threads can go at once

#store in memory of the server


currentPlayer = 0

while True:
    #continuously look for connections
    #socket.accept() = Accept a connection. The socket must be bound to an address and 
    # listening for connections. The return value is a pair (conn, address) 
    # where conn is a new socket object usable to send and receive data on the 
    # connection, and address is the address bound to the socket on the other end of the connection.
    conn, addr = s.accept() # accepts any incoming connection
    print("Connected to:",addr)
    #_thread.start_new_thread(function, args[, kwargs]) =
    #start a new thread and return the identifier
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1