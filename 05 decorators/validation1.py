import functools


def to_int(name, minimum=None, maximum=None):
    def _to_int(function):
	@functools.wraps(function)
	def __to_int(**kwargs):
	    value = int(kwargs.get(name))
	    if minimum is not None:
		assert value >= minimum, ("%s should be >= %r, but is %r" % (name, minimum, value))
	    if maximum is not None:
		assert value <= maximum, ("%s should be <= %r, but is %r" % (name, maximum, value))
	    return function(**kwargs)
	return __to_int
    return _to_int

@to_int("a", minimum=10)
@to_int("b", maximum=50)
def spam(a, b):
    print("a", a)
    print("b", b)

spam(a=11, b=49)
spam(a=9, b=51)

