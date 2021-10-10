def fact(n):
    k = 1
    if n == 0:
        yield 1
    else:
        for i in range(n):
            k = k * (i + 1)
            yield k


for el in fact(10):
    print(el)
    