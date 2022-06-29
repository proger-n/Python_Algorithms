# Функции
def hello():
    print('hello')

hello() # вызов функции
f = hello # присваивание функции
f() # вызов присвоенной

def hello_2(name='John'):
    print('hello ', name)
    return name # прекращается и возвращает то что указано

# по умолчанию функция работает синхронно, т.е. при вызове другой функции ждет результата от нее
# call stack - место где хранятся адреса вызванных функции по очереди, максимум можно до 1000 или
# 10.000 функций вызывать
# функции могут быть вложенными, вызывать себя или другие внутри себя

# Структурное программирование
# проектировать сверху вниз свой код, т.е. постепенно угляблятьч=ся в детали строительства
# творчество и придумывание, потом реализация шага, пото опять и так много раз вглубь
# всегда сперва представить общую картину, потом углубляюсь все дальше и дальше

# 1
def build_home(place, size, price):
    fff


# 2
def build_home(place, size, price):
    def call_manger():
    def call_architector()

# 3

# метод грубой силы, брудфорс, решать влоб, перебором
# как правило применяется на первой итерации при поиске решения