import functools

print "--- function decorators:"

def function_decorator(function):
    @functools.wraps(function)
    def _func1(*args, **kwargs):
	print("%r %r %r" % (function.__name__, args, kwargs))
	return function(*args, **kwargs)

    return _func1

@function_decorator
def function1(arg1, arg2, arg3):
    return str.format("aaa %s, %s, %s " % (arg1, arg2, arg3))

print function1.__name__
print function1.__doc__

print function1("bbb", 2, arg3="3")

print "--- memorization"

def memorize(function):
    function.cache = dict()
    @functools.wraps(function)
    def _memorize(*args):
	if args not in function.cache:
	    function.cache[args] = function(*args)
	return function.cache[args]
    return _memorize

@memorize
def fibonacci(n):
    if n < 2:
	return n
    return n + fibonacci(n-1)

for i in range(1, 7):
    print " %s: %s " % (i, fibonacci(i))
#print fibonacci.__wrapped__.cache
