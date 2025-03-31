# 1 
# 2  3 
# 4  5  6 
# 7  8  9  10 
# 11 12 12 14 15

count = 0
for m in range(1, 6):
    for n in range(1, 6):
        if m >= n:
            count = count + 1
            print(count,end=" ")
        else:
            print(' ', end=" ")
    print()