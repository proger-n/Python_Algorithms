# 1. Дано число n, от 1 до 40
# необходимо вычислить n-е число Фибоначчи

def fib(n):
    # put your code here
    f1, f2 = 0, 1
    for i in range(1, n):
        f1, f2 = f2, f1 + f2

    return f2

def main():
    n = int(input())
    print(fib(n))

main()



# 2. Дано число n, от 1 до 10^7
# необходимо найти последнюю цифру n-го числа Фибоначчи, за менее чем 3 секунды

def fib_digit(n):
    f1, f2 = 0, 1
    digit = 0
    for i in range(1, n):
        f1, f2 = f2 % 10, (f1 + f2) % 10

    return f2


def main():
    n = int(input())
    print(fib_digit(n))

main()