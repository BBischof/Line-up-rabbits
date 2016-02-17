def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

def powerset(elements):
    if len(elements) > 0:
        head = elements[0]
        for tail in powerset(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []

@memoize
def power(n):
    if n > 0:
        elements = range(1, n+1)
        head = elements[0]
        for tail in powerset(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []