# 1 Task
# Входные данные
# В первой строке входных данных задано единственное целое число t (1≤t≤10^4) — количество наборов входных данных.
# Каждый набор входных данных является строкой, содержащей единственное целое число m (1≤m≤10^9) — стоимость товара.
#
# Выходные данные
# Для каждого набора входных данных выведите в отдельной строке единственное целое число d (0≤d<m) такое,
# что если уменьшить стоимость товара на d бурлей, стоимость товара окажется максимально возможным круглым числом.
# Более формально: m−d=10^k, где k — максимально возможное неотрицательное целое число.

A = [1, 2, 178, 20, 999999999, 9000, 987654321]
k = 0
B = []
for m in A:
    for i in range(0, 10):
        if int(m) < 10**i:
            print(m, ' ', 10**(i-1))
            B.append(m-10**(i-1))
            break

print(B)

