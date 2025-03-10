# Write a program to input name,2 subject marks
# calculate total,avg
# find grade based on avg marks
# avg&gt;90 ==&gt; A
# avg&gt;=70&lt;=90 ==&gt; B
# avg&gt;=50&lt;70 ==&gt; C
# avg&lt;50 ==&gt; D


name = input("Enter any name : ")
sub1 = int(input('Enter subject 1 marks :'))
sub2 = int(input('Enter subject 2 marks :'))

total = sub1 + sub2
avg = total/2
result = "pass" if sub1 > 40 and sub2 > 40 else "fail"

print(name, total, avg, result)