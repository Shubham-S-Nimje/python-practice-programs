#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

for m in range(1,6,1):
    for n in range(5,0,-1):
        if n <= m:
            print(n, end=" ")
        else:
            print(' ', end=" ")
    print()