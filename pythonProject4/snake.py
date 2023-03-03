import math


def decorator(func):
    def _():
        print('До вызова')
        result = func()
        print('После вызова')
        return result
    return _


def some_function():
    print('Вызвана какая-то функция')
    return 'Результат'


some_function = decorator(some_function)


print(some_function())
math.degrees()
math.radians()
round(9.0, 1)