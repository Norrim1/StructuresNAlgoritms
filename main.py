import timeit
import matplotlib.pyplot as plt


def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
""" b = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2]
c = [1, 2, 3, 4, 2, 1, 3, 4]
d = [1, 2, 3, 4]
e = [1, 2]
f = [1]

Функция сортирует массив, меняя в парах меньшее с большим значением 
On2 т.к. цикл в цикле(внутренний цикл производится j раз для каждой итерации внешнего цикла)


results = [timeit.timeit('foo(f)', number=100, globals=globals()),
           timeit.timeit('foo(e)', number=100, globals=globals()),
           timeit.timeit('foo(d)', number=100, globals=globals()),
           timeit.timeit('foo(c)', number=100, globals=globals()),
           timeit.timeit('foo(b)', number=100, globals=globals()),
           timeit.timeit('foo(a)', number=100, globals=globals())]

count = [1, 2, 4, 8, 16, 17]

plt.plot(count, results)
plt.show() just in case"""
