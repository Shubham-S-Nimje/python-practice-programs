# Module3.py
def count_vowels(s):
    c=0
    for ch in s:
        if ch in "aeiouAEIOU":
            c=c+1
    return c

def isprime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False

def iseven(num):
    if num%2==0:
        return True
    else:
        return False
    

# Module4.py
# Write a program to find given number is prime or not

from module3 import isprime


num=int(input("Enter any number "))
res=isprime(num)
if res:
    print("Prime")
else:
    print("Not Prime")

# Output
# Enter any number 5
# Prime

# Enter any number 9
# Not Prime

