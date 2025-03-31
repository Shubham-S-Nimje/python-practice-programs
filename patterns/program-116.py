#         * 
#       *
#     * 
#   *
# *


for m in range(1, 6):
    for n in range(6,0,-1):
        if m == n:
            print('*',end=" ")
        else:
            print(' ', end=" ")
    print()