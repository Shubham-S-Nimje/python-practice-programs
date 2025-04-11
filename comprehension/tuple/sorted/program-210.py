# Python – Row-wise element Addition in Tuple Matrix

'''
Input : test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1, 2]

Output : [[('Gfg', 3, 1)], [('best', 1, 2)]]
'''

test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1, 2]

for i in range(len(test_list)):
    for j in range(len(test_list[i])):
        a=list(test_list[i][j])
        a.append(cus_eles[i])
        test_list[i][j]=tuple(a)

print(test_list)
