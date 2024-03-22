import time


def limiter(time_limit, calls_limit):
    def decorator(func):
        calls = []

        def wrapper(*args, **kwargs):
            time_now = time.time()
            calls.append(time_now)

            calls_err = [call for call in calls if call > time_now - time_limit]

            if len(calls_err) > calls_limit:
                raise Exception('Exceeded maximum number of calls')

        return wrapper

    return decorator


@limiter(time_limit=10, calls_limit=2)
def function():
    return 'Hello!'
