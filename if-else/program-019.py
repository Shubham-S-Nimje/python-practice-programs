# Write a program to display &quot;Hello&quot; if a number
# entered by user is multiple of five otherwise print &quot;Bye&quot;

number = int(input("Enter number :"))

if number % 5 == 0:
    print(f"Hello")
else:
    print(f"Bye")