import timeit
import matplotlib.pyplot as plt

def first_find_max_min(a):
    #On, т.к. проходимся в цикле 1 раз
    max = a[0]
    min = a[0]

    for i in a:
        if i > max:
            max = i
        elif i < min:
            min = i
    
    return max, min

def second_find_max_min(a):
    #OlogN от метода sorted
    sorted_list = sorted(a)
    max = sorted_list[-1]
    min = sorted_list[0]
    return max, min

"""a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
b = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2]
c = [1, 2, 3, 4, 2, 1, 3, 4]
d = [1, 2, 3, 4]
e = [1, 2]
f = [1]

results_first = [timeit.timeit('first_find_max_min(f)', number=100, globals=globals()),
           timeit.timeit('first_find_max_min(e)', number=100, globals=globals()),
           timeit.timeit('first_find_max_min(d)', number=100, globals=globals()),
           timeit.timeit('first_find_max_min(c)', number=100, globals=globals()),
           timeit.timeit('first_find_max_min(b)', number=100, globals=globals()),
           timeit.timeit('first_find_max_min(a)', number=100, globals=globals())]

results_second = [timeit.timeit('second_find_max_min(f)', number=100, globals=globals()),
           timeit.timeit('second_find_max_min(e)', number=100, globals=globals()),
           timeit.timeit('second_find_max_min(d)', number=100, globals=globals()),
           timeit.timeit('second_find_max_min(c)', number=100, globals=globals()),
           timeit.timeit('second_find_max_min(b)', number=100, globals=globals()),
           timeit.timeit('second_find_max_min(a)', number=100, globals=globals())]


count = [1, 2, 4, 8, 16, 17]


plt.plot(count, results_first)
plt.plot(count, results_second)
plt.show()  just in case"""
