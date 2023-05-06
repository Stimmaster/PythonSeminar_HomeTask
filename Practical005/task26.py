# Задача 26:  Посчитать факториал(произведение 1 до N) и треугольное число
# (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
#
# Решение:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def triangularNumber(n):
    if n == 0:
        return 0
    else:
        return n + triangularNumber(n-1)

print("Введите целое положительное число n")
n = int(input('Введите число: '))
print()
print("Факториал числа n ревен:", factorial(n))
print("Треугольное число от 1 до n равно:", triangularNumber(n))
print()
