# Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to

# the following criteria :
# Unit                                      # Price
# First 100 units                          # no charge
# Next 100 units                          # Rs 5 per unit
# After 200 units                          # Rs 10 per unit

# (For example if input unit is 350 than total bill amount is Rs2000)


nou = int(input("Enter number of units :"))

if nou <= 100:
    print(f"no charge")
elif nou >100 & nou <= 200:
    print(f"Rs 5 per unit : {nou * 5}")
else:
    print(f"Rs 10 per unit : {nou * 10}")