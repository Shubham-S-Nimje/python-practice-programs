#         A 
#       A B A  
#     A B C B A  
#   A B C D C B A 
# A B C D E D C B A 
#   A B C D C B A 
#     A B C B A  
#       A B A  
#         A 

count = 4
x = 65
y = 67
for m in range(65, 70):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(65, m + 1):
        print(chr(o),end=" ")
    if m!=65:
        for p in range(x, 64, -1):
            print(chr(p), end=" ")
        x=x+1
    count = count - 1
    print()
count = 1
for m in range(68, 64, -1):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(65, m + 1):
        print(chr(o),end=" ")
    if m!=65:
        for p in range(y, 64, -1):
            print(chr(p), end=" ")
        y=y-1
    count = count + 1
    print()
