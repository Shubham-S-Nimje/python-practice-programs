# *       * 
# *       * 
# *       *
# *       *
# *       * 


for m in range(1, 6):
    for n in range(1, 6):
        if n == 1 or n == 5:
            print('*',end=" ")
        else:
            print(' ', end=" ")
    print()