import heapq
import json

heap = [3, 45, 8, 7, 9, 1, 2, 21, 30, 4565, 5, 4567]

heapq.heapify(heap)

print json.dumps(heap, sort_keys=True, indent=4)

while heap:
    print " %s, (%s) " % (heapq.heappop(heap), heap)
