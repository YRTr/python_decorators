def shout(func):
    def wrapper():
        res = func()
        return res.upper()
    return wrapper

@shout
def greet():
    return 'hello world'

print(greet())