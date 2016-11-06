import bisect

l1 = []
l1.append(5)
l1.append(2)
l1.append(1)
l1.append(6)
l1.append(11)
print l1

l1.sort()
print l1

l2 = []
bisect.insort(l2, 5)
bisect.insort(l2, 12)
bisect.insort(l2, 6)
bisect.insort(l2, 11)
bisect.insort(l2, 1)
print l2

l2i =bisect.bisect_left(l2, 11)
print "l2 [ %s ] = %s" % (l2i, l2[l2i])