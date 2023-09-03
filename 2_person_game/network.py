import socket
import pickle #serializes objects

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #in command prompt use command "ipconfig" then look for "IP64"
        #public ip for server
        self.server = "76.20.82.68"#IPV4: 10.0.0.132, Classic: 127.0.0.1, IPV6: 73.151.178.122
        self.port = 5555 #80, 443, 5555 is usually an open port
        self.addr = (self.server, self.port)
        self.p = self.connect()
        """print(self.id)"""
        
    def getP(self):
        return self.p
    
    def connect(self):
        try:
            #connect to the server
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))#load byte data encrypts
        except:
            pass

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data)) #dump to pickle object
            return pickle.loads(self.client.recv(2048))#grabbing object
        except socket.error as e:
            print(e)

"""#test it out
n = Network()
print(n.send("hello"))
print(n.send("working"))"""
        