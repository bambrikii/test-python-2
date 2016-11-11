import functools
import heapq
import pprint

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 145)
heapq.heappush(heap, 16)
heapq.heappush(heap, 11)

pprint.pprint(heap, width=40)
print heapq.nsmallest(10, heap)

heap2 = []
push2 = functools.partial(heapq.heappush, heap2)
smallest2 = functools.partial(heapq.nsmallest, iterable=heap2)

push2(5)
push2(3)
push2(12)
print smallest2(len(heap2))
