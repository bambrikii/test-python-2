import collections
import pprint

print "--- list defaultdict"

dict1 = dict()
dict1[1] = "123"
dict1[3] = "456"

arr1 = []

dict2 = collections.defaultdict(list)
for k, v in dict1.items():
    dict2[k].append(v)

dict2[1].append("789")

pprint.pprint(dict2)

print "--- counter, int defaultdict"

counter = collections.defaultdict(int)
counter[1] += 1
counter["asd"] += 2
counter["asd"] += 1.1E+5
pprint.pprint(counter)

print "--- tree, tree defaultdict"


def tree():
    return collections.defaultdict(tree)


colours = tree()

colours["gray"]["dark"] = 0
colours["gray"]["light"] = 1
colours["gray"]["average"] = 2

pprint.pprint(colours)

import json

print(json.dumps(colours, sort_keys=True, indent=4))
