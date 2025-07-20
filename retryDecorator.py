# Retry Decorator
from functools import wraps
count = 0

def retry(n):
    def multiple(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < n:
                try:
                    res = func(*args, **kwargs)
                except ValueError as v:
                    attempts += 1
                    print(f'Retry {attempts} for {func.__name__} due to {v}')
                else:
                    return res
            print(f'{func.__name__} failed after {n} retries')
            raise v
        return wrapper
    return multiple

@retry(3)
def flaky():
   global count
   count += 1
   if count < 10:
       raise ValueError("Still Failing")
   return "Success"

print(flaky())
