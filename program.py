from math import sqrt
from typing import Optional, Union


def add_numbers(number1: int, number2: int) -> int:
    """Возвращает сумму двух чисел."""
    return number1 + number2


def calculate_square_root(number: int) -> float:
    """Возвращает квадратный корень числа."""
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    """Возвращает строку с квадратным корнем числа, если оно положительное."""
    if your_number <= 0:
        return 'root = 0'

    square_root = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого '
            f'вами числа. Это будет: {square_root}')


num1: int = 10
num2: int = 5
print('Сумма чисел: ', add_numbers(num1, num2))
print(calc(25.5))
