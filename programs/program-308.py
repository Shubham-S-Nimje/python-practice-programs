# Shopping Cart

contact={}
while True:
    print("1.Add Contact")
    print("2.Update Contact")
    print("3.Remove Contact")
    print("4.View all contacts")
    print("5.Exit")
    opt=int(input("Enter Your Option "))

    if opt==1:
        cname=input("Enter contact name : ")
        if cname not in contact:
            cnumber=int(input("Enter contact number : "))
            contact[cname]=cnumber
            print("Contact Added")
        else:
            print(f'{cname} exists within contacts')
    elif opt==2:
        cname=input("Enter contact name : ")
        if cname in contact:
            cnumber=int(input("Updated contact number :"))
            contact[cname]=cnumber
            print("Contact number updated")
        else:
            print(f'{cname} not exists in contact')
    elif opt==3:
        cname=input("Contact name to delete :")
        if cname in contact:
            del contact[cname]
            print("Contact Deleted from contacts")
        else:
            print(f'{cname} not exists within contact')
    elif opt==4:
        print("****Contacts*****")
        for cname,cnumber in contact.items():
            print(f'{cname}\t{cnumber}')
    elif opt==5:
        print('Bye')
        break
    else:
        print("Invalid Option Try Again...")
