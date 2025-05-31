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
window.title("User Register")
window.geometry("400x300+300+200")
window['bg']="green"

lbl1=tkinter.Label(window,text="Name",font=("Arial",15),fg="red",bg="green")
lbl2=tkinter.Label(window,text="UserName",font=("Arial",15),fg="red",bg="green")
lbl3=tkinter.Label(window,text="Password",font=("Arial",15),fg="red",bg="green")

lbl1.place(x=80,y=50)
lbl2.place(x=80,y=100)
lbl3.place(x=80,y=150)

e1=tkinter.Entry(window,width=15,font=("Arial",15),fg="blue")
e2=tkinter.Entry(window,width=15,font=("Arial",15),fg="blue")
e3=tkinter.Entry(window,width=15,font=("Arial",15),fg="blue",show='*')

e1.place(x=200,y=50)
e2.place(x=200,y=100)
e3.place(x=200,y=150)

def register():
    name=e1.get()
    uname=e2.get()
    pwd=e3.get()
    cmd="insert into user_register values(%s,%s,%s)"
    try:
        c.execute(cmd,params=(name,uname,pwd))
        tkinter.messagebox.showinfo(title="info",message="User Registered")
        cn.commit()
        e1.delete(0,tkinter.END)
        e2.delete(0,tkinter.END)
        e3.delete(0,tkinter.END)
    except Exception as e:
        print("Registration Error:", e)
        tkinter.messagebox.showerror(title="error",message="Error in register")
        
def close():
    window.destroy()
    

b1=tkinter.Button(window,text="Register",font=("Arial",15),command=register)
b2=tkinter.Button(window,text="Close",font=("Arial",15),command=close)

b1.place(x=80,y=200)
b2.place(x=200,y=200)

window.mainloop()