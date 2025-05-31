# Bank Client

import socket
while True:
    s=socket.socket()
    s.connect(("localhost",70))
    print("1.Deposit")
    print("2.Withdraw")
    print("3.FindBal")
    print("4.Exit")
    opt=int(input("Enter your option :"))
    if opt==1:
        accn=input("Account No:")
        tamt=input("Transaction Amount:")
        msg=str(1)+" "+accn+" "+tamt
        s.send(msg.encode())
        b=s.recv(1024)
        print(b.decode())
    elif opt==2:
        accn=input("Account No:")
        tamt=input("Transaction Amount:")
        msg=str(2)+" "+accn+" "+tamt
        s.send(msg.encode())
        b=s.recv(1024)
        print(b.decode())
    elif opt==3:
        accn=input("Account No:")
        msg=str(3)+" "+accn
        s.send(msg.encode())
        b=s.recv(1024)
        print(b.decode())
    elif opt==4:
        break
    s.close()
