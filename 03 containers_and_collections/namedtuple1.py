import collections

Tu1 = collections.namedtuple("Tu1", ["a", "b", "c"])

tu1 = Tu1(1, 2, 3)
print tu1

tu2 = Tu1(c=1, b=2, a=3)
print tu2

a, b, c = tu1
print "%s, %s, %s" % (a, b, c)
