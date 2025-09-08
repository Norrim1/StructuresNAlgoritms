import timeit
import matplotlib.pyplot as plt

def del_(a):
    b = a.copy() #Добавляет On
    del b[0]
    return a

"""B теории: Для списков On т.к. после удаления элементы передвигаются на 1(в данном худшем варианте), для словарей O1 т.к. просто удаляется 1 ключ
B итоге из-за копирования сложности алгоритмов O2n и On+1, но эта разница на данных малых количествах элементов видна, но на больших количествах всё сведётся к On в обоих вариантах
(Без копирования просто опустошает список/удаляет 1 ключ из словаря и провести замеры не удастся)

a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
b = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2]
c = [1, 2, 3, 4, 2, 1, 3, 4]
d = [1, 2, 3, 4]
e = [1, 2]
f = [1]

g = {0: 1, 1: 2, 2: 3, 3: 4, 4: 2, 5: 1, 6: 3, 7: 4, 8: 3, 9: 5, 10: -2, 11: -2, 12: 2, 13: -2, 14: 65, 15: 2, 16: 2}
h = {0: 1, 1: 2, 2: 3, 3: 4, 4: 2, 5: 1, 6: 3, 7: 4, 8: 3, 9: 5, 10: -2, 11: -2, 12: 2, 13: -2, 14: 65, 15: 2}
i = {0: 1, 1: 2, 2: 3, 3: 4, 4: 2, 5: 1, 6: 3, 7: 4}
j = {0: 1, 1: 2, 2: 3, 3: 4}
k = {0: 1, 1: 2}
l = {0: 1}

results_first = [timeit.timeit('del_(f)', number=500, globals=globals()),
           timeit.timeit('del_(e)', number=500, globals=globals()),
           timeit.timeit('del_(d)', number=500, globals=globals()),
           timeit.timeit('del_(c)', number=500, globals=globals()),
           timeit.timeit('del_(b)', number=500, globals=globals()),
           timeit.timeit('del_(a)', number=500, globals=globals())]

results_second = [timeit.timeit('del_(l)', number=500, globals=globals()),
           timeit.timeit('del_(k)', number=500, globals=globals()),
           timeit.timeit('del_(j)', number=500, globals=globals()),
           timeit.timeit('del_(i)', number=500, globals=globals()),
           timeit.timeit('del_(h)', number=500, globals=globals()),
           timeit.timeit('del_(g)', number=500, globals=globals())]


count = [1, 2, 4, 8, 16, 17]


plt.plot(count, results_first)
plt.plot(count, results_second)
plt.show()"""