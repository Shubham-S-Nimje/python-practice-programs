def smart_division(function):
    def wrapper(n1,n2):
        if n2==0:
            return 0
        else:
            n3=function(n1,n2)
            return n3
    return wrapper

@smart_division
def division(n1,n2):
    n3=n1/n2
    return n3

num1=int(input("Enter First Integer "))
num2=int(input("Enter Second Integer "))
num3=division(num1,num2)
print(f'{num1}/{num2}={num3:.2f}')
