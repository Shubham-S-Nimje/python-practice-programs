# 1 2 3 4 5 1 
#  1 2 3 4 1 
#   1 2 3 1  
#    1 2 1  
#      1 


count = 0
for m in range(6, 0, -1):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(1, m + 1):
        if o == m or o == m:
            print(1,end=" ")
        else:
            print(f'{o}  ',end=" ")
    count = count + 1
    print()
