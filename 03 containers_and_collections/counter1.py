import collections

str1 = "asda"
counter = collections.Counter(str1)
print counter
for k in str1:
    print " %s %d " % (k, counter[k])

print "--- sqrt"

counter2 = collections.Counter()

import math
for i in range(10):
    v = math.sqrt(i)//2
    counter2[v] += 1
    print "%d, %d; %d -> %d" % (i, math.sqrt(i), v, counter2[v])