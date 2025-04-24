# >>> courses_dict={'java':2000,'python':6000,'c++':2000}
# >>> print(courses_dict)
# {'java': 2000, 'python': 6000, 'c++': 2000}
# >>> c1=courses_dict.popitem()
# >>> print(c1)
# ('c++', 2000)
# >>> c2=courses_dict.popitem()
# >>> print(c2)
# ('python', 6000)
# >>> print(courses_dict)
# {'java': 2000}
# >>> c3=courses_dict.popitem()
# >>> print(c3)
# ('java', 2000)
# >>> c4=courses_dict.popitem()
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     c4=courses_dict.popitem()
# KeyError: 'popitem(): dictionary is empty'
# >>> print(courses_dict)
# {}
