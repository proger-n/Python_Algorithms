import numpy as np

# a = np.array([[3, 2, 4, 4], [2, 4, 3, 3], [2, 1, 3, 1], [4, 3, 3, 4]])
# print(a)
# b = np.array([[2, 4, 1, 2, 4, 4, 3, 2], [3, 2, 4, 1, 3, 1, 1, 4], [1, 2, 1, 1, 2, 3, 4, 2], [3, 1, 3, 3, 1, 3, 3, 4]])
# print(b)
# print(np.matmul(a, b))
def donats():
    s1, s2, s3 = map(int, input().split())
    assert (s1 > 0) & (s2 > 0) & (s3 > 0)

    a = np.empty((s1, s2), dtype='float64')
    for i in range(s1):
        s = input()
        a[i] = np.fromstring(s, dtype='float64', sep=' ')

    b = np.empty((s2, s3), dtype='float64')
    for i in range(s2):
        s = input()
        b[i] = np.fromstring(s, dtype='float64', sep=' ')

    return np.matmul(a, b)


for i in donats():
    for k in i:
        print(k, end=' ')
    print()

# 4 4 8
# 3 2 4 4
# 2 4 3 3
# 2 1 3 1
# 4 3 3 4
# 2 4 1 2 4 4 3 2
# 3 2 4 1 3 1 1 4
# 1 2 1 1 2 3 4 2
# 3 1 3 3 1 3 3 4