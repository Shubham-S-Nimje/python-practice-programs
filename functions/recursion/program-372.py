def print_num(num):
    if num>1: # base case/condition
        print_num(num-1) # recursive case
    print(num)


print_num(3)
