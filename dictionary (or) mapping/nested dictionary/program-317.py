employees_info={101:{'ename':'naresh','sal':45000},
                102:{'ename':'suresh','sal':25000},
                103:{'ename':'kishore','sal':35000}}

emp1=employees_info[101]
emp2=employees_info[102]
emp3=employees_info[103]

print(emp1)
print(emp2)
print(emp3)
print(emp1['ename'],emp1['sal'])
print(emp2['ename'],emp2['sal'])
print(emp3['ename'],emp3['sal'])

print(employees_info[101]['ename'],employees_info[101]['sal'])
