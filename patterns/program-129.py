#         e 
#       e d e  
#     e d c d e  
#   e d c b c d e 
# e d c b a b c d e 

count = 4
x = 101
for m in range(101, 96, -1):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(101, m - 1, -1):
        print(chr(o),end=" ")
    if m!=101:
        for p in range(x, 102, 1):
            print(chr(p), end=" ")
        x=x-1
    count = count - 1
    print()
