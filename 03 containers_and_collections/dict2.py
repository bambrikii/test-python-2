data = dict()
data[1] = "one"
data[2] = "two"
data[3] = "one"
key1 = 4, 5, 6
data[key1] = "one"
key2 = 7,8,9,10,11,12,13
data[key2] = key2

print data

print "--- dict iteration"

for k, v in data.items():
#for k, v in data.iteritems():
    print "k, v : ", k, v

print data[3]
print data[4, 5, 6]
print data[key2]

print "--- tuple iteration"

for i in key2:
    print i