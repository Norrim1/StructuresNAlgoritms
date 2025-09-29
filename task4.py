import timeit
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def fib_with_lucas(n):
    if n < 2:
        return fibonacci(n)
    i = n // 2
    j = n - i
    Fi = fib_with_lucas(i)
    Fj = fib_with_lucas(j)
    Li = lucas(i)
    Lj = lucas(j)
    return (Fi * Lj + Fj * Li) // 2

def lucas_with_fib(n):
    if n == 0:
        return 2 
    return fibonacci(n - 1) + fibonacci(n + 1)

numbers = list(range(10))
results_fib_with_lucas = []
results_lucas_with_fib = []

for n in numbers:
    t1 = timeit.timeit(lambda: fib_with_lucas(n))
    results_fib_with_lucas.append(t1)

    t2 = timeit.timeit(lambda: lucas_with_fib(n))
    results_lucas_with_fib.append(t2)

plt.plot(numbers, results_fib_with_lucas, label="fibonacci_with_lucas")
plt.plot(numbers, results_lucas_with_fib, label="lucas_with_fib")
plt.legend()
plt.show()
