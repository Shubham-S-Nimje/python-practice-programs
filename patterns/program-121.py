#     * 
#    * *  
#   * * *  
#  * * * * 
# * * * * * 

count = 4
for m in range(1, 6):
    for n in range(1, count + 1):
        print(' ',end=" ")
    for o in range(1, m + 1):
        print('*  ',end=" ")
    count = count - 1
    print()


