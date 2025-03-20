# Q2. Write a program to accept the cost price of a bike and display 
# the road tax to be paid according
# to the following criteria :

# Cost price (in Rs)                    # Tax
# > 100000                              # 15 %
# > 50000 and <= 100000                 # 10%
# <= 50000                              # 5%


price = int(input("Enter bike price :"))

if 50000 < price <= 100000:
    tax = price * 0.10
    print(f"10% tax is {tax} total {price+tax}")
elif price <= 50000:
    tax = price * 0.05
    print(f"5% tax is {tax} total {price+tax}")
else:
    tax = price * 0.15
    print(f"15% tax is {tax} total {price+tax}")