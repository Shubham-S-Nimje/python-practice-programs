
# * * * * * 
#  * * * * 
#   * * *  
#    * *  
#     * 

count = 0
for m in range(6, 0, -1):
    for n in range(0, count):
        print(' ',end=" ")
    for o in range(1, m):
        print('*  ',end=" ")
    count = count + 1
    print()


