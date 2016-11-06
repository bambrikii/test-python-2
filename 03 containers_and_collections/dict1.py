def ind(val):
    while val >= 10:
	val //= 10;
    return val;

def add(coll, key, value):
    index = ind(key)
    coll[index].append((key, value))

def contains(coll, key):
    index = ind(key)
    for k, v in coll[index]:
	if k == key:
	    return True
    return False

def print_coll(coll):
    for index in range(len(coll)):
	print " index : ", index
	for k, v in coll[index]:
	    print " k, v : ", k, v

#coll = [[] ] * 10
coll = [[], [], [], [], [], [], [], [], [], []]
print coll

add(coll, 123, "asd")
add(coll, 321, "qwe")
add(coll, 456, "zxc")
add(coll, 457, "zxc")
add(coll, 458, "zxc")
add(coll, 459, "zxc")
print coll

print contains(coll, 459)

print_coll(coll)