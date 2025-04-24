grade_dict={'Naresh':'A',
            'Suresh':'B',
            'Ramesh':'A',
            'Rajesh':'A',
            'Kishore':'C',
            'Kiran':'C'}

print(grade_dict)

grade_dictA={name:grade for name,grade in grade_dict.items()
             if grade=='A'}
print(grade_dictA)
grade_dictB={name:grade for name,grade in grade_dict.items()
             if grade=='B'}
print(grade_dictB)
grade_dictC={name:grade for name,grade in grade_dict.items()
             if grade=='C'}
print(grade_dictC)
