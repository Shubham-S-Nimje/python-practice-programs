def draw_dollars(function):
    def wrapper():
        print("$"*30)
        function()
        print("$"*30)
    return wrapper

def draw_stars(function):
    def wrapper():
        print("*"*30)
        function()
        print("*"*30)
    return wrapper

@draw_stars
@draw_dollars
def display():
    print("PYTHON PROGRAMMING")


display()
