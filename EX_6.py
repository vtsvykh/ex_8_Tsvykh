def show_result(func):
    def wrapper(arg):
        print(f'Результат работы функции {func.__name__}: {func(arg)}.')

    return wrapper


@show_result
def squaring(num):
    result = num ** 2

    return result


@show_result
def is_odd(num):
    if num % 2 != 0:
        return f'{num} - нечётное'
    return f'{num} - чётное'
