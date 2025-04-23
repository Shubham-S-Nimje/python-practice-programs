# Dictionary with items. Within curly braces each item is separated with , 
# and each item contains key and value, which is separated with :

# Syntax: {key:value,key:value,key:value,key:value,…}


# >>> D2={1:10,2:20,3:30,4:40,5:50}
# >>> print(D2,type(D2))
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50} <class 'dict'>
# >>> persons={'naresh':50,
#          'suresh':40,
#          'kishore':45}
# >>> print(persons)
# {'naresh': 50, 'suresh': 40, 'kishore': 45}
# >>> sales={2020:45000,
#        2021:56000,
# ...        2022:65000,
# ...        2023:76000,
# ...        2024:65000}
# >>> print(sales)
# {2020: 45000, 2021: 56000, 2022: 65000, 2023: 76000, 2024: 65000}
# >>> students={'naresh':'python',
# ...           'suresh':'java',
# ...           'kishore':'oracle'}
# >>> print(students)
# {'naresh': 'python', 'suresh': 'java', 'kishore': 'oracle'}
# >>> A={1:10,1:20,1:30,1:40}
# >>> print(A)
# {1: 40}
# >>> B={'a':'apple',
# ...    'b':'ball',
# ...    'b':'box'}
# >>> print(B)
# {'a': 'apple', 'b': 'box'}
# >>> C={1:10,2:10,3:10,4:10,5:10}
# >>> print(C)
# {1: 10, 2: 10, 3: 10, 4: 10, 5: 10}

# One key is mapped with one or more than one value, in order to map with multiple values, these multiple values are stored or put inside collection.

# >>> employees={'naresh':['manager',50000],
# ...            'suresh':['clerk',65000],
# ...            'rajesh':['hr',80000]}
# >>> print(employees)
# {'naresh': ['manager', 50000], 'suresh': ['clerk', 65000], 'rajesh': ['hr', 80000]}
# >>> marks={'naresh':[60,70,80],
# ...        'suresh':[40,50,60],
# ...        'ramesh':[60,80,90]}
# >>> print(marks)
# {'naresh': [60, 70, 80], 'suresh': [40, 50, 60], 'ramesh': [60, 80, 90]}

