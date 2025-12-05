import numpy


def task1():
    array_ = numpy.array([1, 7, 13, 105])
    print(f"Занимаемая массивом память: {array_.nbytes} байт")
    numpy.savetxt('array.txt', array_, delimiter=' ')
    numpy.save('array.npy', array_)
    loaded_txt_array = numpy.loadtxt('array.txt', delimiter=' ')
    loaded_bin_array = numpy.load('array.npy')
    print(f"Массив из txt файла: {loaded_txt_array}")
    print(f"Массив из бинарного файла: {loaded_bin_array}")


def task2():
    print(numpy.zeros(10))
    print(numpy.ones(10))
    print(numpy.ones(10) * 5)


def task3():
    print(numpy.arange(30, 70, 2))


def task4():
    print(numpy.linspace(5, 50, 10))


def task5():
    print(numpy.random.randint(1, 100, (3, 3, 3)))


def task6():
    print(numpy.arange(30, 42).reshape(3, 4))


def task7():
    array_ = numpy.zeros((10, 10))
    array_[0, :] = 1
    array_[9, :] = 1
    array_[:, 0] = 1
    array_[:, 9] = 1
    print(array_)


def task8():
    array_ = numpy.arange(1, 6)
    array_ = numpy.diag(array_)
    print(array_)


def task9():
    array_ = numpy.zeros((4, 4))
    array_[1::2, ::2] = 1
    array_[::2, 1::2] = 1
    print(array_)


def task10():
    print(numpy.arange('2017-03-01', '2017-04-01', dtype ='datetime64'))


def task2_1(array_1, array_2):
    return numpy.intersect1d(array_1, array_2)


def task2_2(array_):
    return numpy.unique(array_)


def task2_3(array_):
    unique_numbers, count = numpy.unique(array_, return_counts=True)
    return unique_numbers, count


def task2_4(array_):
    return numpy.tile(array_, 1), numpy.tile(array_, 2), numpy.tile(array_, 3)


def task2_5(array_):
    flattened = array_.flatten()
    return array_.flatten()[~numpy.isnan(flattened)]


def task2_6(array_, k):
    array_ = numpy.sort(array_)
    return array_[:k]


def task2_7(array_, target_num):
    return array_[numpy.argmin(numpy.abs(array_ - target_num))]


def task2_8(array_1, array_2):
    temp = numpy.char.add(array_1, " ")
    result = numpy.char.add(temp, array_2)
    return result

def task2_9(array_):
    p_counts = numpy.zeros(len(array_))
    for i, s in enumerate(array_):
        p_counts[i] = s.count('P')
    return p_counts

def task2_10(array_):
    return numpy.roots(array_)


def task3():
    array_1, array_1_1, array_1_2, array_2 = [], [], [], []
    for i in range(1, 3):
        for j in range(1, 4):
            if i == 1:
                if j == 3:
                    temp_input_value = input(f'b{i}')
                    array_2 = numpy.append(array_2 ,temp_input_value)
                else:
                    temp_input_value = input(f'a{i}{j}')
                    array_1_1 = numpy.append(array_1_1, temp_input_value)
            else:
                if j == 3:
                    temp_input_value = input(f'a{i}')
                    array_2 = numpy.append(array_2, temp_input_value)
                else:
                    temp_input_value = input(f'a{i}{j}')
                    array_1_2 = numpy.append(array_1_2, temp_input_value)
    array_1 = numpy.append(array_1, [[array_1_1]])
    array_1 = numpy.append(array_1, [[array_1_2]])
    print(array_1)

def task3():
    a = numpy.zeros((2, 2))
    b = numpy.zeros(2)
    for i in range(2):
        for j in range(2):
            a[i, j] = float(input(f"a{i+1}{j+1}: "))
        b[i] = float(input(f"b{i+1}: "))
    print(a)
    print(b)
    det = numpy.linalg.det(a)
    print(det)
    if abs(det) == 0:
        print("Система не имеет решения или имеет их бесконечно много решений(Определитель = 0)")
    else:
        solution = numpy.linalg.solve(a, b)
        print(f"x = {solution[0]}, y = {solution[1]}")


print(task2_1(numpy.arange(1, 6), numpy.arange(4, 8)))
print(task2_2(numpy.array([1, 1, 2, 2,  3, 4, 5, 5, 6, 6])))
print(task2_3(numpy.array([1, 1, 2, 2,  3, 4, 5, 5, 6, 6])))
print(task2_4(numpy.arange(1, 5)))
print(task2_5(numpy.array([[1, 2, 3], [numpy.nan, 0, numpy.nan], [6, 7, numpy.nan]])))
print(task2_6(numpy.array([1, 7, 8, 2, 0.1, 3, 15, 2.5]), 4))
print(task2_7(numpy.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49]), 3.09))
print(task2_8(numpy.char.array(['Python', 'PHP']), numpy.char.array(['Java', 'C++'])))
print(task2_9(numpy.char.array(['Python', 'PHP', 'JS', 'examples', 'html'])))
print(task2_10(numpy.array([1, -4, 7])))
print(task2_10(numpy.array([1, -11, 9, 11, -10])))
task3()



