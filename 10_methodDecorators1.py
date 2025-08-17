"""
Write a class Calculator with:
A method add(self, a, b) decorated to log its call (handle self)
A @staticmethod subtract(a, b) decorated to log its call
A @classmethod info(cls) that prints the class name, also logged
"""

from functools import wraps

def logger_add(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f'Calling {func.__name__} on {self}')
        return func(self, *args, **kwargs)
    return wrapper

def logger_sub(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

def logger_info(func):
    @wraps(func)
    def wrapper(cls, *args, **kwargs):
        print(f'Calling {func.__name__} on class {cls.__name__}')
        return func(cls, *args, **kwargs)
    return wrapper

class Calculator:
    #instance method
    @logger_add
    def add(self, a, b):
        return a+b

    #static method
    @staticmethod
    @logger_sub
    def subtract(a,b):
        return a-b

    #class mmethod
    @classmethod
    @logger_info
    def info(cls, msg):
        return f'{cls.__name__} says {msg}'

c = Calculator()
print(c.add(121,78))
print(Calculator.subtract(55, 11))
print(Calculator.info('Calculations'))
