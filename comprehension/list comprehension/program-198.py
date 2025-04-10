grade_list=[['naresh','A'],
            ['suresh','B'],
            ['ramesh','C'],
            ['kishore','A'],
            ['rajesh','B'],
            ['kiran','B']]


grade_listA=[stud for stud in grade_list if stud[1]=='A']
grade_listB=[stud for stud in grade_list if stud[1]=='B']
grade_listC=[stud for stud in grade_list if stud[1]=='C']

print(f'Student List {grade_list}')
print(f'Student A List {grade_listA}')
print(f'Student B List {grade_listB}')
print(f'Student C List {grade_listC}')
