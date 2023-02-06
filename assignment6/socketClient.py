import socket 
#define socket object, (socket family type, TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#connects to local host to receive message
s.connect((socket.gethostname(), 9999))

msg = s.recv(100)
print(msg.decode("utf-8"))