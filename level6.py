# Time Measurement Decorator
from functools import wraps
import time
def timer(f):
    @wraps(f)
    def wrapper():
        pre = time.time()
        f()
        post = time.time()
        diff = abs(post - pre)
        print(f'Executed {f.__name__} in {diff:.2f} seconds')
    return wrapper

@timer
def wait():
    time.sleep(2)

wait()