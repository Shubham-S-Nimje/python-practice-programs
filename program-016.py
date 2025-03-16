# Write a program to login with OTP NO
import random
name = input("Enter name :")
otp = random.randint(1000,9999)

print(f"Hi! {name}, please enter {otp} OTP")

eotp = int(input("OTP :"))

if eotp == otp:
    print(f"verified")
else:
    print(f"wront OTP")