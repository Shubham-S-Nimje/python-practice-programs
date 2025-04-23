# >>> persons={'naresh':50,
#          'suresh':40,
#          'ramesh':35,
#          'rajesh':55}
# >>> age1=persons.setdefault('naresh')
# >>> print(age1)
# 50
# >>> age2=persons.setdefault('ramesh')
# >>> print(age2)
# 35
# >>> age3=persons.setdefault('rajesh',65)
# >>> print(age3)
# 55
# >>> age4=persons.setdefault('kishore',30)
# >>> print(age4)
# 30
# >>> print(persons)
# {'naresh': 50, 'suresh': 40, 'ramesh': 35, 'rajesh': 55, 'kishore': 30}
# >>> age5=persons.setdefault('kiran')
# >>> print(age5)
# None
# >>> print(age5)
# None
# >>> print(persons)
# {'naresh': 50, 'suresh': 40, 'ramesh': 35, 'rajesh': 55, 'kishore': 30, 'kiran': None}
