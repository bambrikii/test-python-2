import pprint
import collections

arr1 = {x*y for y in range(3) for x in [1, 2, 3]}
pprint.pprint(arr1, width=40)

arr2 = set([x+y for x in range(3) for y in range(3)])
pprint.pprint(arr2, width=40)

arr3 = [1, 1, 1, 2, 3]
c1 = collections.Counter(arr3)
pprint.pprint(c1)
