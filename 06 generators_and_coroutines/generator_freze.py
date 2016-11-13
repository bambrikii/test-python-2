def generator():
    print('Before 1')
    yield 1
    print('After 1')

    print('Before 2')
    yield 2
    print('After 2')

    print('Before 3')
    yield 3
    print('After 3')


g = generator()
print('Got %d' % next(g))
print("---")
print('Got %d' % next(g))
print("---")
