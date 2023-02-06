import socket 
#define socket object, (socket family type, TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#binds to local host and port
s.bind((socket.gethostname(), 9999))
#queues up incoming messages
s.listen(5) 
#check for connections forever
while True:
    clientsocket, address = s.accept()
    #print("A message from CS361!")
    #clientsocket.send(bytes("A message from CS361", "utf-8"))