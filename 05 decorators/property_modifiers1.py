class Cls1(object):
	def __init__(self, arg1=1):
		print "Cls1.__init__(%s, %s)" % (self, arg1)
		self.arg1 = arg1
	def __get__(self, instance, cls):
		print "Cls1.__get__(%s, %s, %s)" % (self, instance, cls)
		return self.arg1
	def __set__(self, instance, value):
		print "Cls1.__set__(%s, %s, %s)" % (self, instance, value)
		self.arg1 = value

class Cls2(object):
	prop2 = Cls1(3)
	def __init__(self, arg2):
		self.prop2 = arg2

obj2 = Cls2(1)
print obj2.prop2
obj2.prop2 = 2
print obj2.prop2

