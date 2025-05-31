# Banking Server

import socket

print("NIT BANK")
print("Server is Running")
customers={1:["naresh",50000],
           2:["suresh",65000],
           3:["ramesh",80000],
           4:["kishore",75000],
           5:["kiran",54000]}

s=socket.socket()
s.bind(('localhost',70))
s.listen(5)
while True:
    t=s.accept()
    client=t[0]
    b=client.recv(1024*2)
    msg=b.decode()
    data=msg.split()
    if len(data)==0:
        msg="Thanks"
    else:
        match(int(data[0])):
            case 1:
                accno,tamt=int(data[1]),float(data[2])
                if accno in customers:
                    customers[accno][1]+=tamt
                    msg="transaction completed"
                else:
                    msg="invalid accno"
            case 2:
                accno,tamt=int(data[1]),float(data[2])
                if accno in customers:
                    if customers[accno][1]>tamt:
                        customers[accno][1]-=tamt
                        msg="transaction completed"
                    else:
                        msg="insuff balance"
                else:
                    msg="invalid accno"
            case 3:
                accno=int(data[1])
                if accno in customers:
                    bal=customers[accno][1]
                    msg=str(bal)
                else:
                    msg="invalid accno"
    client.send(msg.encode())
    client.close() 