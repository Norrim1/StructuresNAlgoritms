def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1 #Всё остальное (сценарии(возвращение значения)) базовый
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3) #Рекурсивный (т.к. снова вызов)
    
print(tribonacci(3))