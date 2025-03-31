# 1 2 3 4 5 
#   2 3 4 5
#     3 4 5
#       4 5
#         5

for m in range(1,6,1):
    for n in range(1,6,1):
        if n >= m:
            print(n, end=" ")
        else:
            print(' ', end=" ")
    print()