# You are creating a traffic light simulation program.

# The light color can be 'Red', 'Yellow', or 'Green.'
# If the color is 'Red,' print 'Stop.'
# If the color is 'Yellow,' print 'Get Ready.'
# If the color is 'Green,' print 'Go.'
# Write a Python program to implement this logic using
# match..case

color=input('Enter color :')
match(color):
    case 'Red':
        print('Stop')
    case 'Yellow':
        print('Get Ready')
    case 'Green':
        print('Go')
    case _:
        print('Invalid Color')