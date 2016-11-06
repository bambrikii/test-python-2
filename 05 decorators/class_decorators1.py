import functools

class Debug(object):
	def __init__(self, function):
		self.function = function
		functools.update_wrapper(self, function)
	def __call__(self, *args, **kwargs):
		output = self.function(*args, **kwargs)
		print ("%s(%r, %r): %r" % (self.function.__name__, args, kwargs, output))
		return output

@Debug
def func1(args1):
	return 'func1' * (args1 % 5)

print func1(3)
