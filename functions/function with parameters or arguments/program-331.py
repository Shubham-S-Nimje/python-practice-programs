def simple_interest(amt,t,rate): # required parameters
    si=(amt*t*rate)/100
    print(f'Simple Interest {si:.2f}')



simple_interest(5000,12,1.2) # Positional Arguments
simple_interest(amt=9000,t=24,rate=1.5) # Keyword Arguments
simple_interest(rate=1.7,amt=10000,t=28) # Keyword Arguments
