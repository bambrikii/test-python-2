import functools

class Cls1(object):
	def __init__(self, value):
		print "%s" % (value)
		self.value = value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __eq__(self, other):
		return self.value == other.value

	def __repr__(self):
		return "{0}".format(self.value)

class Cls2(Cls1):
	def __gt__(self, other):
		return self.value < other.value

	def __ge__(self, other):
		return self.value <= other.value

	def __lt__(self, other):
		return self.value > other.value

	def __le__(self, other):
		return self.value >= other.value

	def __eq__(self, other):
		return self.value == other.value

@functools.total_ordering
class Cls3(Cls1):
	def __lt__(self, other):
		return self.value < other.value

	def __eq__(self, other):
		return self.value == other.value

numbers = [6, 1.1, 45, 11, 32]

arr1 = [Cls2(n) for n in numbers]
print sorted(arr1)

arr2 = [Cls3(n) for n in numbers]
print sorted(arr2)

