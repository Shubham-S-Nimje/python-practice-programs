# Server Program

import socket
s=socket.socket()
s.bind(("localhost",50))
s.listen(5)
print("Server is Running...")
t=s.accept()
client=t[0]
b=client.recv(1024)
msg=b.decode()
print(msg)
msg="Hello Client"
client.send(msg.encode())
s.close()