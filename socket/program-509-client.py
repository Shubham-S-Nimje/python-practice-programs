# Client Program

import socket
s=socket.socket()
s.connect(("localhost",50))
msg="Hello Server"
b=msg.encode()
s.send(b)
b=s.recv(1024)
print(b.decode())
s.close()