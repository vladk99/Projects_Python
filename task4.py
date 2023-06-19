# Multi-paradigm movie programming
# Lab Work 2.
# Koshma Vladyslav IKM-221a
from utils import inp_variable


def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]


if __name__ == '__main__':
    print('Multi-paradigm movie programming', 'Lab Work 2')
    print('Koshma Vladyslav', 'IKM-221a')
    print(is_palindrome(inp_variable('x', 'Enter your number', float)))
