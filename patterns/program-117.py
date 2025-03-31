#         * 
#       *
#     * 
#   *
# *


for m in range(1, 6):
    for n in range(1, 6):
        if m == n or m+n == 6:
            print('*',end=" ")
        else:
            print(' ', end=" ")
    print()