class Cls1(object):
	def __init__(self):
		print "initializing..."
		self.registry = {}
		self.attr1 = "val1"


	def __setattr__(self, key, value):
		if key == "registry":
			object.__setattr__(self, key, value)
		else:
			print "settings attribute %s to %s" % (key, value)
			self.registry[key] = value;

	def __getattr__(self, key):
		if hasattr(self.registry, key):
			val = self.registry[key]
			print "getting attribute %s, value is %s" % (key, val)
			return val
		else:
			print "no attribute %s exists, won't get" % (key)
			return None

	def __delattr__(self, key):
		if hasattr(self.registry, key):
			val = self.registry[key]
			print "deleting attribute %s with value %s" % (key, val)
			del self.registry[key]
		else:
			print "no attribute %s exists, won't delete" % (key)
			return

cls1 = Cls1()
print cls1.attr2
cls1.att2 = "asd"
print cls1.attr2
del cls1.attr2
print cls1.attr2
	
