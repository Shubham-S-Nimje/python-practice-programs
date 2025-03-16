# Write a program to find input amount is multiples of
# 500 or not

amount = int(input("Enter amount :"))
r = amount%500

if r==0:
    print(f"Allow to withdraw")
else:
    print(f"pleae enter amount multiple of 500")