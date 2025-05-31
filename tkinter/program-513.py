import tkinter
import mysql.connector
import tkinter.messagebox

from dotenv import load_dotenv
import os

load_dotenv()

cn=mysql.connector.connect(database= os.getenv('MYSQL_NAME'),
                   user= os.getenv('MYSQL_USER'),
                   password= os.getenv('MYSQL_PASSWORD'),
                   host= os.getenv('MYSQL_HOST'),
                   port= os.getenv('MYSQL_PORT'))

print("connection established...")

c=cn.cursor()

window=tkinter.Tk()
window.title("Login")

l1=tkinter.Label(window,text="UserName",font=("Arial",20))
l2=tkinter.Label(window,text="Password",font=("Arial",20))

e1=tkinter.Entry(window,width=15,font=("Arial",20))
e2=tkinter.Entry(window,width=15,font=("Arial",20),show="$")

def login():
    username=e1.get()
    password=e2.get()
    cmd="select * from user_register where username=%s and password=%s"
    c.execute(cmd,params=(username,password))
    row=c.fetchone()
    if row==None:
        tkinter.messagebox.showinfo(title="info",message="Invalid username or password")
    else:
        tkinter.messagebox.showinfo(title="info",message=f'{username} welcome')
        window.destroy()
        w1=tkinter.Tk()
        w1.title("Transaction")
        w1.geometry("300x300")
    

def close():
    window.destroy()


b1=tkinter.Button(window,text="Login",font=("Arial",20),command=login)
b2=tkinter.Button(window,text="Close",font=("Arial",20),command=close)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
b1.grid(row=3,column=1)
b2.grid(row=3,column=2)

window.mainloop()