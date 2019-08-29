def call_once(func):
    cache, is_called = None, False

    def wrapper(*args, **kwargs):
        nonlocal cache, is_called
        if not is_called:
            cache = func(*args, **kwargs)
            is_called = True
        return cache
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
