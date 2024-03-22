import json
import xmltodict
import yaml


def to_format(format=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if format == 'json' or format is None:
                return json.dumps(result)
            elif format == 'xml':
                return xmltodict.unparse({'data': result})
            elif format == 'yaml':
                return yaml.dump(result)

        return wrapper

    return decorator


@to_format(format='xml')
def get_data(name, surname, city):
    return {'name': name, 'surname': surname, 'city': city}
