class Cls1(object):
	def get_prop1(self):
		print "get prop1"
		return self._prop1
	def set_prop1(self, prop1):
		print "set prop1"
		self._prop1 = prop1
	def delete_prop1(self):
		print "delete prop1"
		del self._prop1
	prop1 = property(get_prop1,set_prop1,delete_prop1)

	@property
	def prop2(self):
		print "setting prop2"
		return self._prop2
	@prop2.setter
	def prop2(self, prop2):
		print "getting prop2"
		self._prop2 = prop2
	@prop2.deleter
	def prop2(self):
		print "deleting prop2"
		del self._prop2

some_prop = Cls1()

print "--- prop1 "

some_prop.prop1 = 123
print some_prop.prop1
del some_prop.prop1

print "--- prop2 "

some_prop.prop2 = 123
print some_prop.prop2
del some_prop.prop2
