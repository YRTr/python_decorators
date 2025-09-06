# Retry Decorator
from functools import wraps
count = 0

def retry(n):
    def multiple(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            local_error_handling = None
            for attempts in range(1, n+1):
                try:
                    return func(*args, **kwargs)
                except ValueError as v:
                    local_error_handling = v
                    if attempts < n:
                        print(f'Retry {attempts} for {func.__name__} due to {v}')
                    else:
                        print(f'{func.__name__} failed after {n} attempts')
                        raise
            if local_error_handling is not None:
                raise local_error_handling
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
