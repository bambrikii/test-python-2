
import functools

def singleton(cls):
	instances = dict()
	@functools.wraps(cls)
	def _singleton(*args, **kwargs):
		if cls not in instances:
			print "initializing %s" % (cls)
			instances[cls] = cls(*args, **kwargs)
		else:
			print "%s already initialized" % (cls)
		return instances[cls]
	return _singleton

@singleton
class Cls1(object):
	def __init__(self):
		print "init"


cls1 = Cls1()
cls2 = Cls1()

