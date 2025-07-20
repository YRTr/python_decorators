# Decorator with Arguments in the Wrapped function

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args:{args} kwargs:{kwargs}')
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a,b):
    return a+b

add(3,4)