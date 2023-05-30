# Multi-paradigm movie programming
# Lab Work 2.
# Koshma Vladyslav IKM-221a
import math as m

TEMPLATE = 'Input {} = '


# check for invalid known numbers
def validate_inp(variable_name, incorrect_value):
    while True:
        variable_val = inp_variable(variable_name, TEMPLATE)
        if variable_val != incorrect_value:
            return variable_val
        print(f'Input incorrect, {variable_name} != {incorrect_value}')


# number check
def inp_variable(values, template):
    while True:
        try:
            return float(input(template.format(values)))
        except ValueError:
            print('Enter not number')

-
def raw_input():
    x = inp_variable('x', TEMPLATE)
    y = validate_inp('y', y_incorrect)
    z = inp_variable('z', TEMPLATE)
    r = ((x + z) / 8) / (18.2 - m.pow(3.8, y) + 19.3)
    print(r)


if __name__ == '__main__':
    print('Multi-paradigm movie programming', 'Lab Work 2')
    print('Koshma Vladyslav', 'IKM-221a')
    y_incorrect=(-2 * m.log(5) - m.log(3) + m.log(2)) / (m.log(5) - m.log(19))
    print(y_incorrect)
    raw_input()
