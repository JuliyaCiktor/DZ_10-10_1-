import types
def some_gen(begin, end, func):
    """
    Генератор числової послідовності.

    :param begin: перший елемент послідовності
    :param end: кількість елементів у послідовності
    :param func: функція, яка формує наступне значення для послідовності
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

def pow(x):
    return x ** 2
gen = some_gen(2, 4, pow)

# Тести
assert isinstance(gen, types.GeneratorType), 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
