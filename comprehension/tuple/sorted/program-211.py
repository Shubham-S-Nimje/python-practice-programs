# Python – Remove Tuples of Length K
'''
Input:test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)],
K = 2 
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
Explanation : (4, 5) of len = 2 is removed.
'''

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K=2
i=0
while True:
    if i==len(test_list):
        break
    if len(test_list[i])==K:
        del test_list[i]
        continue
    i=i+1
    
print(test_list)
