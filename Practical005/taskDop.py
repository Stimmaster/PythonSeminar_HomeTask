# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи
#
# Решение:

n = int(input("Введите номер числа Фибоначчи: "))


def fibonachiNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachiNumber(n-1) + fibonachiNumber(n-2)


fibonacci = fibonachiNumber(n)
print("N-е число Фибоначчи равно: ", fibonacci)
