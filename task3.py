# Multi-paradigm movie programming
# Lab Work 3.
# Koshma Vladyslav IKM-221a
import math as m

TEMPLATE = 'Input {} = '


def validate_inp(variable_name, incorrect_value, incorrect_value2):
    while True:
        variable_val = inp_variable(variable_name, TEMPLATE)
        if (variable_val != incorrect_value) and (variable_val != -incorrect_value) and (
                variable_val != incorrect_value2):
            return variable_val
        print(f'Input incorrect, {variable_name} != {incorrect_value}, {-incorrect_value}')


def inp_variable(values, template):
    while True:
        try:
            return float(input(template.format(values)))
        except ValueError:
            print('Enter not number')


def raw_input():
    x = validate_inp('x', y_incorrect, 0)
    if (m.log(x ** 2)) <= 4:
        return print('Enter user incorrect < 4')
    r = ((m.log(x ** 2)) - 4) ** 1 / 2
    print(r)


if __name__ == '__main__':
    print('Multi-paradigm movie programming', 'Lab Work 2')
    print('Koshma Vladyslav', 'IKM-221a')

    y_incorrect = 5 ** (1 / 2)
    raw_input()
