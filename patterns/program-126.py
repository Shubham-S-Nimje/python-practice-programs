#         1 
#       1 2 1  
#     1 2 3 2 1  
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 

count = 4
x = 1
for m in range(1, 6):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(1, m + 1):
        print(o,end=" ")
    if m!=1:
        for p in range(x, 0, -1):
            print(p, end=" ")
        x=x+1
    count = count - 1
    print()
