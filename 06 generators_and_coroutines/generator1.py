print 'generator 1'


def count(start=0, step=1, stop=10):
    n = start
    while n < stop:
        yield n;
        n += step


for x in count(10, 2.5, 20):
    print(x)

print 'generator 3'


def generator3(n):
    i = 0
    while i < n:
        i += 1
        yield i;


for i in generator3(5):
    print i;

print 'generator 2'


def generator():
    yield 'generator 1'
    return  # 'generator 1 return'


g = generator()
next(g)
next(g)

# generator()
