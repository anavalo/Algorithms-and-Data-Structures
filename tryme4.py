def new_line():
    print('.')


def three_lines():
    new_line()
    new_line()
    new_line()


# printing 9 lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# printing 25 lines
def clear_screen():
     nine_lines()
     nine_lines()
     three_lines()
     three_lines()
     new_line()

nine_lines()
clear_screen()
