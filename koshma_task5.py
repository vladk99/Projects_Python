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

e = 1e-4
result = calculate_sum(e)
print(f"The sum of the series with accuracy {e} is: {result}")

n = int(input("Введіть ціле число: "))
digit_count = len(str(abs(n)))
print(f"Кількість цифр у числі {n}: {digit_count}")
