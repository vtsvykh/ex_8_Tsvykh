input_string = input('Введите строку: ')
start, end = map(int, input('Введите начало и конец: ').split())


def is_upper(item):
    return item.isupper()


out_filter = list(filter(is_upper, input_string[start - 1: end]))
print(f'Обнаружено: {len(out_filter)} симв. в верхнем регистре: {out_filter}.')
