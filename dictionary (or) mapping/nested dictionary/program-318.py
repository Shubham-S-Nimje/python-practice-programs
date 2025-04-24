marks_details={1:[50,60],
               2:[60,70],
               3:[70,80],
               4:[80,90]}

print(marks_details[1][0],marks_details[1][1])
print(marks_details[2][0],marks_details[2][1])
print(marks_details[3][0],marks_details[3][1])

marks_details={1:{'sub1':50,'sub2':60},
               2:{'sub1':60,'sub2':70},
               3:{'sub1':70,'sub2':80},
               4:{'sub1':80,'sub2':90}}

print(marks_details[1]['sub1'],marks_details[1]['sub2'])
print(marks_details[2]['sub1'],marks_details[2]['sub2'])
print(marks_details[3]['sub1'],marks_details[3]['sub2'])
