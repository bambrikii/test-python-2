import itertools


def list1():
    yield "elem1"
    yield "elem2"


a, b = itertools.tee(list1())

print("a")
print(next(a))
print(next(a))

print("b")
print(next(b))
print(next(b))
