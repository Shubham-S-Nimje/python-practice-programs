# Creating tuple with multiple values, multiple values are separated with ,

# >>> t5=(10,20,30,40,50)
# >>> print(t5,type(t5))
# (10, 20, 30, 40, 50) <class 'tuple'>
# >>> stud1=(101,"naresh",5000)
# >>> stud1[-1]=6000
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     stud1[-1]=6000
# TypeError: 'tuple' object does not support item assignment
# >>> del stud1[0]
# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     del stud1[0]
# TypeError: 'tuple' object doesn't support item deletion
# >>> emp1=101,"naresh","HR",50000
# >>> print(emp1,type(emp1))
# (101, 'naresh', 'HR', 50000) <class 'tuple'>
