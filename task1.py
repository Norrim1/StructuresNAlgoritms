import timeit
import matplotlib.pyplot as plt

def sel_sort(arr, start=0):
    if start >= len(arr) - 1:
        return arr
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[start], arr[min_index] = arr[min_index], arr[start]
    sel_sort(arr, start + 1)

def fast_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return fast_sort(left) + middle + fast_sort(right)

random1 = [81, 14, 3, 94, 35, 31, 28, 17]
random2 = [81, 14, 3, 94, 35, 31, 28, 17, 94, 13, 86, 94, 69, 11, 75, 54]
random3 = [81, 14, 3, 94, 35, 31, 28, 17, 94, 13, 86, 94, 69, 11, 75, 54, 4, 3, 11, 27, 29, 64, 77, 22, 51, 66, 54, 29, 85, 94, 49, 60]
random4 = [81, 14, 3, 94, 35, 31, 28, 17, 94, 13, 86, 94, 69, 11, 75, 54, 4, 3, 11, 27, 29, 64, 77, 22, 51, 66, 54, 29, 85, 94, 49, 60,
        3, 27, 96, 73, 42, 70, 58, 24, 60, 99, 56, 5, 80, 12, 78, 72, 80, 48, 71, 80, 77, 18, 29, 80, 93, 20, 7, 71, 40, 10, 37, 65]

sort1 = [0, 1, 2, 3, 4, 5, 6, 7]
sort2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sort3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
sort4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
        32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]

back_sort1 = [8, 7, 6, 5, 4, 3, 2, 1]
back_sort2 = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
back_sort3 = [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
back_sort4 = [64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35,
            34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

amount = [8, 16, 32, 64]
results_random_sel = [timeit.timeit('sel_sort(random1.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(random2.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(random3.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(random4.copy())', globals=globals(), number=100)]

results_random_fast = [timeit.timeit('fast_sort(random1.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(random2.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(random3.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(random4.copy())', globals=globals(), number=100)]

results_sort_sel = [timeit.timeit('sel_sort(sort1.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(sort2.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(sort3.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(sort4.copy())', globals=globals(), number=100)]

results_sort_fast = [timeit.timeit('fast_sort(sort1.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(sort2.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(sort3.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(sort4.copy())', globals=globals(), number=100)]

results_back_sel = [timeit.timeit('sel_sort(back_sort1.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(back_sort2.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(back_sort3.copy())', globals=globals(), number=100),
    timeit.timeit('sel_sort(back_sort4.copy())', globals=globals(), number=100)]

results_back_fast = [timeit.timeit('fast_sort(back_sort1.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(back_sort2.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(back_sort3.copy())', globals=globals(), number=100),
    timeit.timeit('fast_sort(back_sort4.copy())', globals=globals(), number=100)]


plt.plot(results_random_sel, amount, label = "random_sel")
plt.plot(results_random_fast, amount, label = "random_fast")
plt.legend()
plt.show()
plt.plot(results_sort_sel, amount, label = "sort_sel")
plt.plot(results_sort_fast, amount, label = "sort_fast")
plt.legend()
plt.show()
plt.plot(results_back_sel, amount, label = "back_sel")
plt.plot(results_back_fast, amount, label = "back_fast")
plt.legend()
plt.show()