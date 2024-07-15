from typing import Callable, Generator
import re

text = """"Працює з дійсними числами 2 20.01 75.006 на ряду з від'ємними
        дійсними числами - -7 -45.65 та звичайно нулем 0. Також числа
        можна відокремлювати не лише пробілами 63, -85, 89.89."""


def generator_numbers(text: str) -> Generator[float, None, None]:
  pattern = r'\d+\.\d*|-\d+\.\d*|\d+|-\d+'
  for number in re.findall(pattern, text):
    yield float(number)


def sum_profit(text: str, func: Callable) -> float:
  result = 0
  for number in func(text):
    result += number
  return round(result, 2)


print(sum_profit(text, generator_numbers))
