# Accounts.py
customer={}
def create_account():
    accno=int(input("AccountNo :"))
    if accno not in customer:
        cname=input("CustomerName :")
        balance=float(input("Balance :"))
        customer[accno]=[cname,balance]
        return True
    else:
        return False
def update_account():
    accno=int(input("AccountNo to update "))
    if accno in customer:
        cname=input("CustomerName :")
        customer[accno][0]=cname
        return True
    else:
        return False
def delete_account():
    accno=int(input("AccountNo to delete "))
    if accno in customer:
        del customer[accno]
        return True
    else:
        return False
def view_account():
    for accno,cust in customer.items():
        print(f'{accno}-->{cust}')


# Bank.py
from accounts import *

while True:
    print("1.Create Account")
    print("2.Update Account")
    print("3.Delete Account")
    print("4.View Account")
    print("5.Exit")
    opt=int(input("Enter Your Option :"))
    if opt==1:
        b=create_account()
        if b:
            print("Account Created...")
        else:
            print("Account exists")
    elif opt==2:
        b=update_account()
        if b:
            print("Account Updated...")
        else:
            print("Invalid Accno")
    elif opt==3:
        b=delete_account()
        if b:
            print("Account Deleted...")
        else:
            print("Invalid Accno")
    elif opt==4:
        view_account()
    elif opt==5:
        break
    else:
        print("Invalid Option")
    

# Output:
# 1.Create Account
# 2.Update Account
# 3.Delete Account
# 4.View Account
# 5.Exit
# Enter Your Option :1
# AccountNo :101
# CustomerName :naresh
# Balance :45000
# Account Created...
# 1.Create Account
# 2.Update Account
# 3.Delete Account
# 4.View Account
# 5.Exit
# Enter Your Option :4


