import utils
import math

def calculate_sum(e):
    n = 0
    sum = 0

    while True:
        term = (math.factorial(n) ** 2) / (2 ** (n ** 2))
        sum += term

        if term < e:
            break

        n += 1

    return sum


def digit_count(n):
    if n == 0:
        digit_cout = 1
    else:
        digit_cout = int(math.log10(abs(n))) + 1
    return digit_cout
def square_root(number, e):
    x = number  # Початкове наближення
    while True:
        y = (x + number / x) / 2  # Ітераційна формула Герона
        if abs(y - x) < e:  # Перевірка точності
            break
        x = y
    return y

e = 1e-4
result = calculate_sum(e)
print(f"The sum of the series with accuracy {e} is: {result}")

n=utils.inp_variable("n : ", int)
print(f"Кількість цифр у числі {digit_count(n)}")

number = utils.inp_variable("Введіть число: ", float)
result = square_root(number, e)
print(f"Квадратний корінь з числа {number}={result}")
