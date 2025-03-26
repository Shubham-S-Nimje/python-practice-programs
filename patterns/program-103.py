# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1

for m in range(1, 6):
    for n in range(1, 6):
        if n % 2 == 0:
            print(0,end=" ")
        else:
            print(1, end=" ")
    print()