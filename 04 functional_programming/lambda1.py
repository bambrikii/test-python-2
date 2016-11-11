# la = lambda n : n > 0 ? n *
Y = lambda f: lambda *args: f(Y(f))(*args)
a = Y(lambda c: lambda n: n and n * c(n - 1) or 1)(5)

print a

fa = lambda n: n and n * fa(n - 1) or 1
print fa(5)

quicksort = Y(lambda f:
              lambda x: (
                  f([item for item in x if item < x[0]])
                  + [y for y in x if x[0] == y]
                  + f([item for item in x if item > x[0]])
              ) if x else []
              )

qs_result = quicksort([1, 3, 5, 4, 1, 3, 2])
print qs_result
