"""
Write one single generic decorator logger that:
1. Detects what kind of method it is wrapping:
instance method → gets self as the first argument.
class method → gets cls as the first argument.
static method → gets neither self nor cls.

2. Logs accordingly:
If instance → Calling <funcname> on instance of <classname>
If class method → Calling <funcname> on class <classname>
If static method → Calling static <funcname>

3. Works for all three when applied directly
"""
from functools import wraps
import inspect

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            first = args[0]
            if isinstance(first,type):
                print(f'Calling {func.__name__} on class {first.__name__}')
            else:
                print(f'Calling {func.__name__}  on instance of {first.__class__.__name__}')
        else:
            print(f'Calling static {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    @logger
    def add(self,a,b):
        return a+b

    @staticmethod
    @logger
    def sub(a,b):
        return a-b

    @classmethod
    @logger
    def info(cls, msg):
        return f'{cls.__name__} says {msg}'

c = Calculator()
print(c.add(2,3))
print(c.sub(24, 13))
print(c.info('math'))
