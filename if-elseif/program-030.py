# You are building a system for checking the grading system of a student. 

# The grades are based on scores:
# A for scores 90 and above
# B for scores between 70 and 89
# C for scores between 50 and 69
# F for scores below 50

# Write a Python program that takes a score as input and 
# prints the corresponding grade using if..elif.



percentage = float(input("Enter percentage :"))

if percentage >= 90:
    print(f"A grade")
elif 70 <= percentage < 90:
    print(f"B grade")
elif 50 <= percentage < 70:
    print(f"C grade")
else:
    print(f"D grade")