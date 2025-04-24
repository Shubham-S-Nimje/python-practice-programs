# Write a program to read details of n persons
# each person having name,age

n=int(input("How Many Persons?"))
persons={input('Name:'):int(input('Age:')) for i in range(n)}

for name,age in persons.items():
         print(f'{name}-->{age}')
