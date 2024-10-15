
def add_everything_up(a, b):
    try:
        c = a + b
        print(round(c, 4))

    except TypeError:
        print(a, b, sep='')

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
