def print_list(l):
    for i in l:
        print i


def print_cut():
    print "-----------------"


arr = list()
arr.append(1)
print arr
print "arr[0] : ", arr[0]
arr.remove(1)
print arr

print_cut()

str1 = "str1"
print str1[1:3]

print_cut()

str2 = "str2"
print str1 + str2

print_cut()

print_list(str1)

for s in str1:
    print s

print_list(range(len(str1)))
# for i in range(len(str1)):
#    print " % - % " % i, str1[i]

print_cut()
str3 = ""
print "str1 hash: ", str1.__hash__()
