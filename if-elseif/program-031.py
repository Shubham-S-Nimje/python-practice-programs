# In a store, there are discount rules based on the total purchase amount:

# A 10% discount for purchases above $100
# A 5% discount for purchases between $50 and $100
# No discount for purchases below $50

# Write a Python program that takes the purchase amount and prints 
# the appropriate discount.


amount = int(input("Enter amount :"))

if amount > 100:
    discount = amount * 0.10
    print(f"10% discount is {discount} total {amount-discount}")
elif 50 <= amount <= 100:
    discount = amount * 0.05
    print(f"5% discount is {discount} total {amount-discount}")
else:
    print(f"0% discount total {amount}")