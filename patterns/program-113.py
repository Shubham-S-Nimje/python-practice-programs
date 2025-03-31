# * * * * * 
#   * * * *
#     * * *
#       * *
#         *

for m in range(5,0,-1):
    for n in range(5,0,-1):
        if n <= m:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()