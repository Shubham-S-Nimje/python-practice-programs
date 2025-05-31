# Server Program
import socket

s=socket.socket()
s.bind(("localhost",60))
s.listen(5)
print("Server is Running")
s.accept()
print("Connection Established")
s.close()