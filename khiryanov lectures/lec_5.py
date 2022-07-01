# массивы в питоне
# тип list - изменяемый тип данных, содержимое может изменяться, int, float неизменяемые, просто меняется ссылка
A = [1, 2, 3, 4, 5]
for i in range(len(A)):
    A[i] = A[i] ** 2
print(A)

A = [0] * 10
C = A # если так присваивать list, то свызь останется и С будет изменяться при изменении А и наоборот,
      # т.к они оба ссылатся на один list, с одним числом такого не происходит, например x=12 y=x
C = list(A) # так можно сделать несвязанную копию
A[0] = 12
print(C[0])

# задача: ввести последовательно числа, в конце написать 0 и тем самым прекратиться ввод
# затем перевернуть массив задом-наперед
A = [0] * 1000 #
top  = 0 # уровень заполненности массива
x = int(input()) # активатор введения первого числа
while x != 0:
    A[top] = x
    top += 1
    x = int(input())
for k in range(top - 1, -1, -1):
    print(A[k])

# задача. вводиться N-колво элем массива, далее сам массив. скопировать содержимое в другой массив
N = int(input())
A = [0] * N
B = [0] * N
for k in range(N):
    A[k] = int(input())
for k in range(N):
    B[k] = A[k]

# линейный поиск в списке, в массиве
def array_search(A:list, N:int, x:int):
    '''
    Осуществяляет поиск числа х в массиве А
    от 0 до N-1 индекса включительно.

    :param A: массив в котором ищем
    :param N: до этого индекса ищем
    :param x: искомая величина
    :return: индекс первого найденного элемента, -1 если такого элемента нет
    '''
    for k in range(N):
        if A[k] == x:
            return k
    return -1

# пишем тестирование
def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('#test2 - ok')
    else:
        print('#test2 - fail')

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print('#test3 - ok')
    else:
        print('#test3 - fail')

test_array_search()


# Обращение массива, сделать его задом-наперед

def invert_array(A:list, N:int):
    '''
    Обращение массива

    :param A: массив А
    :param N: количество элементов в массиве А
    :return: введенный массив обращается
    '''

    for k in range(N//2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 8)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 - ok')
    else:
        print('#test2 - fail')

test_invert_array()

# Циклический сдвиг влево, вправо наоборот

def left_circle(A:list, N:int):
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k + 1]
    A[N-1] = tmp

A = [1, 2, 3, 4, 5]
left_circle(A, 5)
print(A)

