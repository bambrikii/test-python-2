import operator
import itertools
import pprint

months = [x+1 for x in range(12)]
sum1 = "list(itertools.accumulate(months,operator.add)) # does not work"

pprint.pprint(months,width=40)
pprint.pprint(itertools)
print sum1

# --- chain ---
a = range(3)
b = range(2)
c = list(itertools.chain(a, b))
pprint.pprint(sorted(c))
