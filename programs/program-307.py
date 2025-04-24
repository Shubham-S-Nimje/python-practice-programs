# Shopping Cart

cart={}
while True:
    print("1.Add Product")
    print("2.Update Product")
    print("3.Remove Product")
    print("4.View Cart")
    print("5.Exit")
    opt=int(input("Enter Your Option "))
    if opt==1:
        pname=input("ProductName :")
        if pname not in cart:
            qty=int(input("Qty :"))
            cart[pname]=qty
            print("Product Added")
        else:
            print(f'{pname} exists within cart')
    elif opt==2:
        pname=input("ProductName :")
        if pname in cart:
            qty=int(input("Updated Qty :"))
            cart[pname]=qty
            print("Product Qty Updated")
        else:
            print(f'{pname} not exists in cart')
    elif opt==3:
        pname=input("Product Name to Delete :")
        if pname in cart:
            del cart[pname]
            print("Product Deleted from cart")
        else:
            print(f'{pname} not exists within cart')
    elif opt==4:
        print("****CART*****")
        for pname,qty in cart.items():
            print(f'{pname}\t{qty}')
    elif opt==5:
        print('Happy Shopping')
        break
    else:
        print("Invalid Option Try Again...")
