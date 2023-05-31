# Multi-paradigm movie programming
# Lab Work 2.
# Koshma Vladyslav IKM-221a


def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

# number check
def inp_variable(values, template):
    while True:
        try:
            return float(input(template.format(values)))
        except ValueError:
            print('Enter not number')


if __name__ == '__main__':
    print('Multi-paradigm movie programming', 'Lab Work 2')
    print('Koshma Vladyslav', 'IKM-221a')
    print(is_palindrome(inp_variable('x', 'Enter your number')))