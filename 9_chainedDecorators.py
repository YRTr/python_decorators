from functools import wraps

def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('This is decorator 1: Execute')
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('This is decorator 2: Execute')
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello world!")


greet()

'''
Which decorator runs first during decoration?
=> decorator_two runs first

Which one wraps the function last?
=> decorator_one wraps last

In what order the print statements execute when the function is called?
=> decorator_one, decorator_two, function
'''