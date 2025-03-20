# You are creating a traffic light simulation program. The light color can be "Red", "Yellow", or "Green."
# If the color is "Red," print "Stop."
# If the color is "Yellow," print "Get Ready."
# If the color is "Green," print "Go."

# Write a Python program to implement this logic using if..elif.


color = input("Enter color :")

if color == 'red':
    print(f"Stop")
elif color == 'yellow':
    print(f"Get Ready")
elif color == 'green':
    print(f"Go")
else:
    print(f"Wait...")