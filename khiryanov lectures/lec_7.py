# РЕКУРСИЯ
# Подзадача проще задачи для которой была вызвана предыдущая(вызвавшая) функция, т.е. каждая итерация приближает к результату
# Должен быть 1.рекурентный и 2.крайний случай у рекурсии, чтобы выполнить задачу и не замкнуться
# Глубина рекурсии - это количество самовызовов функции начиная с первого вызова
#
#
#
#
#
#

# def matreshka(n):
#     if n == 1:
#         print('Матрешка')
#     else:
#         print('Верх матрешки n=', n)
#         matreshka(n-1)
#         print('Низ матрешки n=', n)
#
# matreshka(10)

# факториал числа через рекурсию

def f(n):
    assert n >= 0, 'Factorial of negative number not defined'  # проверка на входе, выдаст ошибку если не выполнится
    if n == 0:
        return 1
    return f(n-1) * n

print(f(5))

# НОД

def EuclidGCD_short(a, b):
    '''поиск по алгоритму Евклида лаконично'''
    return a if b == 0 else EuclidGCD_short(b, a%b)

print(EuclidGCD_short(10, 35))

# Быстрое возведение числa в целую неотрицательную степень

def pow_fast(a:float, n:int):
    '''speed - O(log(n))'''
    if n == 0:
        return 1
    elif n%2 == 0:
        return pow(a**2, n//2)
    else:
        return pow(a, n-1) * a

def pow_ordinary(a:float, n:int):
    '''speed - O(n)'''
    if n == 0:
        return 1
    else:
        return pow(a, n-1) * a

print(pow_fast(20, 30))
print(pow_ordinary(20, 30))

# Ханойская башня

