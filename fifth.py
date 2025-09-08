import timeit
import matplotlib.pyplot as plt

def in_(a):
    return 65 in a

"""Для списков сложность On, в то время как в множествах O1, что подтверждается графиком

a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
b = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2]
c = [1, 2, 3, 4, 2, 1, 3, 4]
d = [1, 2, 3, 4]
e = [1, 2]
f = [1]

g = {1, 2, 3, 4, 5, 65, -2}
h = {1, 2, 3, 4, 5, 65, -2}
i = {1, 2, 3, 4}
j = {1, 2, 3, 4}
k = {1, 2}
l = {1}

results_first = [timeit.timeit('in_(f)', number=500, globals=globals()),
           timeit.timeit('in_(e)', number=500, globals=globals()),
           timeit.timeit('in_(d)', number=500, globals=globals()),
           timeit.timeit('in_(c)', number=500, globals=globals()),
           timeit.timeit('in_(b)', number=500, globals=globals()),
           timeit.timeit('in_(a)', number=500, globals=globals())]

results_second = [timeit.timeit('in_(l)', number=500, globals=globals()),
           timeit.timeit('in_(k)', number=500, globals=globals()),
           timeit.timeit('in_(j)', number=500, globals=globals()),
           timeit.timeit('in_(i)', number=500, globals=globals()),
           timeit.timeit('in_(h)', number=500, globals=globals()),
           timeit.timeit('in_(g)', number=500, globals=globals())]


count = [1, 2, 4, 8, 16, 17]


plt.plot(count, results_first)
plt.plot(count, results_second)
plt.show()"""