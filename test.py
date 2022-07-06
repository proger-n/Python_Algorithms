


def main():
    N = int(input())
    A = [True] * N  # изначально положим что числа простые
    A[0] = A[1] = False  # 0 и 1 числа как не простые
    for k in range(2, N):
        if A[k]:
            for m in range(2 * k, N, k):
                A[m] = False

    for k in range(N):
        if A[k]:
            print(k, '-', "простое" if A[k] else "составное")

if __name__ == '__main__':
    main()




