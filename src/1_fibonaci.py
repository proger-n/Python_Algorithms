# 1. Дано число n, от 1 до 40
# необходимо вычислить n-е число Фибоначчи

def fib_slow_cycle(n):
    # put your code here
    f1, f2 = 0, 1
    for i in range(1, n):
        f1, f2 = f2, f1 + f2

    return f2


def fib_slow_recursion(n):
    assert n >= 0
    return n if n <= 1 else fib_slow_recursion(n - 1) + fib_slow_recursion(n - 2)


cache = {}
def fib_fast_recursion(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib_fast_recursion(n - 1) + fib_fast_recursion(n - 2)
    return cache[n]


def memo(f):  # декоратор для функций
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


import time
def timed(f, *args, n_iter=100):  # для измерения времени работы функции
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


from matplotlib import pyplot as plt
def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # n = int(input())
    # # print('fib_slow_cycle', fib_slow_cycle(n))
    # # print('fib_slow_recursion', fib_slow_recursion(n))
    # # print('fib_fast_recursion', fib_fast_recursion(n))
    #
    # fib1 = memo(fib_slow_recursion)  # есть ограничения по глубине рекурсии
    # # print('decorator - memo', fib1(n))
    # fib2 = memo(fib_slow_cycle)  # этот вариант покажет максимум возможного чисел фибоначчи
    # # print('decorator - memo', fib2(n))
    #
    # print('speed of fib_slow_cycle: ', timed(fib_slow_cycle, n))
    # print('speed of fib_fast_recursion: ', timed(fib_fast_recursion, n))
    # print('speed of decorated fib_slow_cycle: ', timed(fib2, n))

    compare([fib_slow_recursion, fib_slow_cycle], list(range(20)))



main()

# для визуализации вызовов рекурсий
# from rcviz import viz
#
# old_fib1 = fib_slow_recursion
# fib_slow_recursion = viz(fib_slow_recursion)
# fib_slow_recursion(5)

# 2. Дано число n, от 1 до 10^7
# необходимо найти последнюю цифру n-го числа Фибоначчи, за менее чем 3 секунды

# def fib_digit(n):
#     f1, f2 = 0, 1
#     digit = 0
#     for i in range(1, n):
#         f1, f2 = f2 % 10, (f1 + f2) % 10
#
#     return f2
#
#
# def main():
#     n = int(input())
#     print(fib_digit(n))
#
# main()






