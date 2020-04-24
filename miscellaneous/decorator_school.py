

### Decorators #################################

from functools import wraps

registry = []

def register(func):
    name = func.__name__
    registry.append(name)
    return func

def add_docstring(func):
    if func.__doc__ is None:
        func.__doc__ = '<missing docstring>'
    return func

def add_logging (func):
    @wraps(func)
    def f(*args):
        print 'Calling',func.__name__,'with',args
        result = func(*args)
        print 'Returning result', result
        return result
    return f

def cache(func):
    answers = {}
    @wraps(func)
    def f(*args):
        if args in answers:
            return answers[args]
        result = func(*args)
        answers[args] = result
        return result
    return f


#### Test Code #################################

import time

@add_logging
@add_docstring
@register            # square = register(square)
def square(x):
    'Return a value times itself'
    return x * x

@add_logging
@add_docstring
@register
@register
def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

@cache
@register
def big_calc(x):
    'Simulate a big calculation'
    print 'Doing hard work'
    time.sleep(1)
    return x + 1


