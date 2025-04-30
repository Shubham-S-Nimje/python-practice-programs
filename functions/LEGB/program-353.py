def calculator(n1,n2,opr):
    res=None # local variable
    def add():
        nonlocal res
        res=n1+n2
    def sub():
        nonlocal res
        res=n1-n2
    def multiply():
        nonlocal res
        res=n1*n2
    def div():
        nonlocal res
        res=n1/n2

    match(opr):
        case '+':
            add()
        case '-':
            sub()
        case '/':
            div()
        case '*':
            multiply()
        case _:
            res="invalid operator"
    return res
    

#main
while True:
    n1=int(input("First Number "))
    n2=int(input("Second Number "))
    opr=input("Enter Operator (off to stop)")
    if opr=="off":
        break
    result=calculator(n1,n2,opr)
    print(f'{n1}{opr}{n2}={result}')
