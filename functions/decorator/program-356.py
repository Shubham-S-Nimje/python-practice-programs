def draw_stars(function):
    def wrapper():
        print("*"*40)
        function()
        print("*"*40)
    return wrapper

@draw_stars
def display():
    print("PYTHON LANGUAGE")

@draw_stars
def print_student_data():
    stud_data={'naersh':'python',
               'suresh':'java',
               'ramesh':'oracle',
               'kishore':'mysql'}
    for name,course in stud_data.items():
        print(f'{name}\t{course}')


display()
print_student_data()
