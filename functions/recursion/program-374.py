def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)



number=int(input("Enter any number "))
result=factorial(number)
print(f'factorial of {number} is {result}')
