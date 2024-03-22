import json


def to_json(func):
    def wrapper(*args, **kwargs):
        print(json.dumps(func(*args, **kwargs)))

    return wrapper


@to_json
def get_data(name, age, city):
    data = {
        'name': name,
        'age': age,
        'city': city
    }
    return data


@to_json
def to_string_json(greet, user_name):
    return f'{greet}, {user_name}!'
