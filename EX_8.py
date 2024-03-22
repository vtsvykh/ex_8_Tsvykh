from datetime import datetime


def get_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as inst:
            with open('log', 'a') as f:
                f.write(f'{datetime.now()}, {type(inst).__name__}\n')

    return wrapper


@get_error
def devider(num_1, num_2):
    return num_1 / num_2


devider(10, 0)
