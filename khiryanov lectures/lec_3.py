# цифра - символ для кодирования числа, математическая абстракция
# число - существует вне зависимости от записи в системе исчисления, из реальности
# бит - это двоичный разряд
# 8 бит - 1 байт(8 пар по 0 или 1) или 2^8=128 вариантов чисел внутри
x = 0b1111 # 0b говорит о том что далее будет записано 2ичное число
y = 0o1111 # 0o говорит о том что далее будет записано 8ричное число
z = 0x1111 # 0x говорит о том что далее будет записано 16ричное число
print(x, y, z) # печатает в 10тичной системе всегда
a = int('z3f', base=36) # число в ковычках и в бэйз= основание, максимум 36ричное
print(a)
b = 127
b = bin(b) # для перевода числа в 2ичную систему из 10ичной, тип str получается
print(b, type(b))
b = oct(127) # для перевода числа в 8ичную систему из 10ичной, тип str получается
print(b)
b = hex(127) # для перевода числа в 16ичную систему из 10ичной, тип str получается
print(b)

# схема Горнера, получение числа по любому основанию из 10чного, записывая остаток от деления
base = int(input('Input base:'))
number = num = int(input('Input number:'))
while number > 0:
    digit = number % base
    if digit == 10:
        digit = 'a'
    elif digit == 11:
        digit = 'b'
    elif digit == 12:
        digit = 'c'
    elif digit == 13:
        digit = 'd'
    elif digit == 14:
        digit = 'e'
    elif digit == 15:
        digit = 'f'
    print(digit, end='')
    number //=base

new_num = []
while num > 0:
    digit = num % base
    if digit == 10:
        digit = 'a'
    elif digit == 11:
        digit = 'b'
    elif digit == 12:
        digit = 'c'
    elif digit == 13:
        digit = 'd'
    elif digit == 14:
        digit = 'e'
    elif digit == 15:
        digit = 'f'
    new_num.append(digit)
    num //=base

print(new_num)

# для нахождения максимума в последовательности
x = [1, 4, 5, 122, 123, 3]
print(x)
m = x[0]
for i in range(len(x)):
    #print(x[i])
    m = max(m, x[i])
print('maximum', m)