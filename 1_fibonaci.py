# def fib(n):
#     # put your code here
#     f1, f2 = 0, 1
#     for i in range(1, n + 1):
#         f1, f2 = f2, f1 + f2
#
#     return f2
#
# def main():
#     n = int(input())
#     print(fib(n))
#
# main()

def fib_digit(n):
    f1 = 0
    f2 = 1
    fibon = 0
    digit = 0
    for i in range(1, n + 1):
        fibon = f1 + f2
        digit = (fibon % 10 + f2 % 10) % 10
        f2 = f1
        f1 = fibon

    return digit


def main():
    n = int(input())
    print(fib_digit(n))

main()