import modules
from modules.fungen import fun_gen
from modules.funname import func_name
from modules.funsum import func_sum
from modules.DZ7 import rename

enter = input('Что будем делать:?\n'
              '1.Добавить числа в строки:\n'
              '2.Генерировать псевдо имена\n'
              '3.Объеденить числа с именами\n'
              '4.Переименовать файлы\n')
if enter == '1':
    quantity = int(input('Какое количество строк будем добавлять?: \n'))
    filename = input('Напишите имя файла с раширением куда будем сохранять\n')
    fun_gen(quantity, filename)
if enter == '2':
    quantity = int(input('Какое количество имен будем генерировать?: \n'))
    filename = input('Напишите имя файла с раширением куда будем сохранять:\n')
    func_name(quantity, filename)
if enter == '3':
    file1 = input('Введите имя файла с числами\n')
    file2 = input('Введите имя файла с именами\n')
    func_sum(file1, file2)
if enter == '4':
    endfile = input('Введите окончание файла\n') 
    extension = input('Файлы с каким расширением будем переименовывать?\n')
    diap = list((input('Какой дипазон будем оставлять от прежнего имени, введите бе пробелов?\n')))
    koldigit = input('Какое кол-во цифр будет перед нумеровкой?')
    extend = input('Введите желаемое расщирение переименованного файла\n')
    print(diap)
    rename(endfile, extension, diap, koldigit, extend)


