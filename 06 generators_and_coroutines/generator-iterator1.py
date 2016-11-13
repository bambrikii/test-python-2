class Count(object):
    def __init__(self, start=0, step=1, stop=10):
        self.n = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):  # Python 2.7
        # def __next__(self): # Python 3.5
        n = self.n
        if n > self.stop:
            raise StopIteration()

        self.n += self.step
        return n


count = Count(10, 2.5, 20)
print(count)

for x in count:
    print(x)
