# НОД найти для 2 целых неотрицательных чисел

def NaiveGCD(a, b):
    '''поиск перебором всех возможных делителей'''
    gcd = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def EuclidGCD(a, b):
    '''поиск по алгоритму Евклида'''
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return EuclidGCD(a % b, b)
    if b >= a:
        return EuclidGCD(a, b % a)


def test_gcd(gcd_algorithm):
    print('Using: ', gcd_algorithm.__doc__)
    print('Test #1: ', end='')
    a, b, gcd_t = 1, 1, 1
    if gcd_algorithm(a, b) == gcd_t:
        print('OK')
    else:
        print('FAIL')

    print('Using: ', gcd_algorithm.__doc__)
    print('Test #2: ', end='')
    a, b, gcd_t = 18, 35, 1
    if gcd_algorithm(a, b) == gcd_t:
        print('OK')
    else:
        print('FAIL')

    print('Using: ', gcd_algorithm.__doc__)
    print('Test #3: ', end='')
    a, b, gcd_t = 288, 192, 96
    if gcd_algorithm(a, b) == gcd_t:
        print('OK')
    else:
        print('FAIL')

    print('Using: ', gcd_algorithm.__doc__)
    print('Test #4: ', end='')
    a, b, gcd_t = 14159572, 63967072, 4
    if gcd_algorithm(a, b) == gcd_t:
        print('OK')
    else:
        print('FAIL')


def main():
    test_gcd(NaiveGCD)
    test_gcd(EuclidGCD)
 #   a, b = map(int, input().split())


if __name__ == "__main__":
    main()
