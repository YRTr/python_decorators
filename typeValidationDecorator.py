# Type Validation Decorator

from functools import wraps
import inspect
def validate_types(dictionary):
    def validator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func).bind(*args, **kwargs)
            sig.apply_defaults()
            for key, val in sig.arguments.items():
                if key in dictionary:
                    expected_val = dictionary[key]
                    if not isinstance(val, expected_val):
                        raise TypeError(f'Argument {key} must be of type {dictionary[key]}')
            return func(*args, **kwargs)
        return wrapper
    return validator

@validate_types({'a': int, 'b': str})
def process(a,b):
    print(f'Received: {a}, {b}')

process(10, 'hello')
# process(10, 20)