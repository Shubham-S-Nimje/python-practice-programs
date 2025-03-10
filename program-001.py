# Write a program to find max of two numbers
num1=int(input('Enter any number :'))
num2=int(input('Enter any number :'))
num3=num1 if num1 > num2 else num2
print(f'max of {num1} and {num2} is {num3}')
      
# >>> a = int(input("Enter number 1 :"))
# Enter number 1 :10
# >>> b = int(input("Enter number 2 :"))
# Enter number 2 :20
# >>> print("a") if a > b else print("b")
# b
# >>> 

# ==================================================

# >>> a = int(input("Enter number 1 :"))
# Enter number 1 :10
# >>> b = int(input("Enter number 2 :"))
# Enter number 2 :20
# >>> print("a") if a > b else print("b")
# b
# >>> c = a  if a > b else b
# >>> c
# 20
# >>> 

