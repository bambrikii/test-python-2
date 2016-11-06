import random
import json
import pprint

arr1 = [x for x in [random.random() for y in range(10)] if x >= 0.5]
print arr1

arr2 = [x for x in range(10)]
print arr2

arr3 = [(x, y) for x in range(2) for y in range(2)]
print json.dumps(arr3, sort_keys = True, indent = 2)

arr4 = [y for x in [3, 4, 5] for y in range(x)]
print json.dumps(arr4, indent = 2)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

reshaped_matrix = [
		    [
			[y for x in matrix for y in x][i * len(matrix) + j]
			for j in range(len(matrix))
		    ]
		    for i in range(len(matrix[0]))
	    ]
pprint.pprint(reshaped_matrix, width=40)
print "%s %s" % (len(matrix), len(matrix[0]))

for x in matrix:
    print " - %s" % x

arr5 =	[
	    [
		[3, 2, 1][0]
	    ]
	]

pprint.pprint(arr5)

arr6 = [y for x in matrix for y in x]
pprint.pprint(arr6)