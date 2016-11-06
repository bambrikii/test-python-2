import functools

def func1(function):
	@functools.wraps(function)
	def _func1(self, n):
		return function(self, n + 1)
	return _func1

class Class1(object):
	@func1
	def func2(self, n = 2):
		return n * 'func2'

cls1 = Class1()
print cls1.func2(3)
