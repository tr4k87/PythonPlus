# Задача 1: Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


# import os

# def path_file(txt):
#     dir, name = os.path.split(txt)
#     path, extension = os.path.splitext(txt)
#     res = (dir, name, extension)
#     return res

# print(path_file('c:/new_folder/text.txt'))

# Задача 2: Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии 

# name = ['Sergey', 'Igor', 'Roman']
# rate = [10000, 50000, 40000]
# bonus = ['10.25%', '6.15%', '12%']

# def bonus_rate(name, rate, bonus):
#     return {name: round(rate*(1+float(bonus.replace('%',''))/100)) for name, rate, bonus in zip(name,rate,bonus)}
    
# print(bonus_rate(name,rate,bonus))

# Задача 3 Создайте функцию генератор чисел Фибоначчи 

# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# print(list(fib(20)))   

# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.



tabl_gen = (print(f'{i}x{j}', end =',') for i in range(2,10) for j in range(2,11))
print(*tabl_gen)
