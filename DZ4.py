# Задача 1 Напишите функцию для транспонирования матрицы

# def trans_matrix(matrix):
#     matrix_t = [list(i) for i in zip(*matrix)]
#     return matrix_t

# my_matrix = [[1,2,3,4], [9,8,7,6]]
# print(trans_matrix(my_matrix))

# Задача 2 Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# def key_arg_only(**kwarg):
#     my_dict = {}
#     for key, value in kwarg.items():
#         my_dict[value] = key
#     return my_dict


# print(key_arg_only(a = 2, b = "Hello", c = 478))

# Задача 3 Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
# oper = int
# count = 0
# cash = 0
# count = 1
# def withdraw(cash):
#     a = int(input('Введите сумму кратную 50 у.е.: '))
#     if a % 50 == 0:
#         if a < cash:
#             cash = cash - a - percent(a)
#             print(f'Вы сняли {a}')
#         else: print(f'Не хватает денег на балансе')
#     else: print('Сумма не кратна 50 у.е.')
#     return cash

# def refil(cash):
#     b = int(input('Какую сумму вы хотите внести?: '))
#     cash = cash + b
#     print(cash)
#     return cash

# def percent(a):
#     perc = a * 0.015
#     print(perc)
#     if perc > 30 and perc  < 300:
#         return perc
#     elif perc < 30:
#         return 30
#     else: return 300


# while oper != 4:
#     oper = int(input('Какую операцию хотите совершить?: \n 1. Снять деньги \n 2. Пополнить баланс \n 3. Баланс\n 4.Выйти\n' ))
#     if cash > 5000000:
#             cash = cash *0.9
#     if count % 3 == 0:
#         print('остаток от деления', count % 3 )
#         cash = cash * 1.03
#         print(f'Баланс: {cash}')
#     if oper == 1:
#         cash = withdraw(cash)
#         print(f'Баланс: {cash}')
#     if oper == 2:
#         cash = refil(cash)
#         print(f'Баланс: {cash}')
#     if oper == 3:
#         print(f'Баланс: {cash}')
#     count += 1

# Дополнительные задачи
# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def plus(my_tuple):
#     res = []
#     for value in my_tuple.values():
#         res.append(value[0] - value[1])
#     if min(res) >= 0: return True
#     else: return False
    
# my_tuple = {'Microsoft' : [20000000, 5456322], 'Gazprom' : [5644231, 6452154], 'Rosneft': [756432156, 345644], 'Magnit': [45632145, 4568877]}
# print(plus(my_tuple))

# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def del_s(**kwarg):
    new_dict = {}
    for key, value in kwarg.items():
        if len(key) > 1:
            for i in key:
                if i == 's':
                    key = key.replace('s', '')
                    value = None  
        print(key, value)
                    
      
del_s(homes = 'Home', air = 'Plane', peoples = 6, s = 45)
