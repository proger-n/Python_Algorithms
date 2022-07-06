# list не является массивом, а объект который изменяет
A = [] # можно так объявить, и потом специальными методами добавлять элементы
A.append(1) # добавить в конец
A.pop() # удалить с конца 1 элемент
A = [x**2 for x in range(10)] # list comprehensions - типа генератор списков

A = [1, 2, 3, 5, 12, 6]
B = [n**2 for n in A if n % 2 == 0] # возвести четные в квадрат
B = [0 if n < 5 else n**2 for n in A if n % 2 == 0] # c тернарным оператором доп отбор на < 5


# сортировки
# 1. О(N^2, не больше)-по скорости. Квадратичные. Бывает асимптотика использ памяти или скорости вычисления
# 1.1. Insert sort(сортировка вставками) - начиная с первой пары меняем местами два соседних элемента по заданному критерию и
#                                          так включая все новые элементы пока не включим все
# 1.2. Choise sort(сортировка методом выбора) - поиск среди всех первого, потом второго среди оставшихся и так до конца
# 1.3. Bubble sort(пузырька) - смотрит строго на два элемента и меняет если не соответ критериям,
#                              и так начинает заново постоянно. у нас отсортировываются с конца

def insert_sort(A):
    """сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    """сортировка списка А выбором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """сортировка списка А методом пузырька"""
    N = len(A)
    for i in range(N):
        for k in range(N-1):
            if A[k + 1] < A[k]:
                A[k], A[k + 1] = A[k + 1], A[k]

def test_sort(sort_algorithm):
    print('Testing ', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'fail')

    print('testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'fail')

    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'fail')



if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
