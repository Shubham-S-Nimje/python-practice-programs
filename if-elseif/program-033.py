# You are building a movie ticket pricing system where the price depends on both age and whether the person has a membership.
# If the person is under 12, the ticket is free regardless of membership.
# If the person is 12-18 and has a membership, the ticket costs $5.
# If the person is 12-18 and does not have a membership, the ticket costs $10.
# If the person is over 18, the ticket costs $15.

# Write a Python function that determines the ticket price based on the person's age and membership status.

age = int(input("Enter age :"))
membership_input = input("Is membership :")
membership = membership_input == 'yes'  

if age < 12:
    print(f"Free")
elif ((12 <= age <= 18) & (membership)):
    print(f"the ticket costs $5")
elif ((12 <= age <= 18) & (not membership)):
    print(f"the ticket costs $10")
else:
    print(f"the ticket costs $15")