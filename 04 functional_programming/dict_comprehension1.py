import pprint

dict1 = {x: x ** 2 for x in range(50) if x % 2 == 0}
pprint.pprint(dict1, width=40)

dict2 = {x * 1.0: [y * 1.0e+100 for y in range(5)] for x in range(3)}
pprint.pprint(dict2, width=40)

# print "%s" % (json.dumps(dict2))
