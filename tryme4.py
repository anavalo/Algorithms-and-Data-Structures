def new_line():
    print('.')


def three_lines():
    new_line()
    new_line()
    new_line()


# function for printing 9 lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# function for printing 25 lines
def clear_screen():
     nine_lines()
     nine_lines()
     three_lines()
     three_lines()
     new_line()

print('Printing nine lines:')
nine_lines()
print('Printing twentyfive lines:')
clear_screen()
