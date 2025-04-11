# Python – Remove Tuples from the List having every element
# as None

test_list=[(None, 2),(None,None),(3, 4),(12, 3),(None,)]
i=0
while True:
    if i==len(test_list):
        break

    t=test_list[i]
    c=t.count(None)
    if c==len(t):
        del test_list[i]
        continue
    i=i+1

print(test_list)
