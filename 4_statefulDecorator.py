#Stateful Decorator (Function Call Counter)

# Write a decorator @call_counter that counts how many times a function was called and prints the count before each call

from functools import wraps
def call_counter(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Call {wrapper.calls} to greet')
        return f(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def greet(name):
    print(f'Hello, {name}')

greet('jack')
greet('john')
greet('jake')