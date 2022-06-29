def fib(n):
    # put your code here
    f1 = 0
    f2 = 1
    fibon = 0
    for i in range(1, n + 1):
        fibon = f1 + f2
        f2 = f1
        f1 = fibon

    return fibon

def main():
    n = int(input())
    print(fib(n))

main()

