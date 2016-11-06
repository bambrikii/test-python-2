import collections

q1 = collections.deque()
for i in range(15):
    q1.append(i)
print "initial ", q1

q1.popleft()
print "popleft ", q1


q1.pop()
print "pop     ", q1
q1.pop()
print "pop     ", q1

print "circular"

circ = collections.deque(maxlen=2)
circ.append(1)
print circ
circ.append(2)
print circ
circ.append(3)
print circ
circ.append(4)
print circ
