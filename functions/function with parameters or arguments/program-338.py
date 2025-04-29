def simple_interest(amt,t,rate=1.5):
    si=(amt*t*rate)/100
    return si


res1=simple_interest(5000,12)
print(f'Simple Interest is {res1:.2f}')
res2=simple_interest(9000,12,1.8)
print(f'Simple Interest is {res2:.2f}')
