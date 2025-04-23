# Login Application

user_details={'naresh':'n123',
              'suresh':'s123@',
              'ramesh':'ramesh123',
              'kishore':'k678@$'}


while True:
    uname=input("UserName :")
    pwd=input("Password :")
    if uname in user_details:
        p=user_details[uname]
        if pwd==p:
            print(f'{uname} Welcome to MyApplication')
            break
        else:
            print("Invalid Password Try Again")
    else:
        print("Invalid Username Try Again")
