import modules
import os
from modules.fungen import fun_gen
from modules.funname import func_name
from modules.funsum import func_sum
from modules.DZ7 import rename
from modules.funcreate import fun_create
from modules.funcreate import create_file
from modules.funsort import fun_sort


enter = input('Что будем делать:?\n'
              '1.Добавить числа в строки:\n'
              '2.Генерировать псевдо имена\n'
              '3.Объеденить числа с именами\n'
              '4.Переименовать файлы\n'
              '5.Создать файлы с генерированными именами\n'
              '6.Создать файлы с разными расширениями\n'
              '7.Сортировать документы\n')
if enter == '1':
    quantity = int(input('Какое количество строк будем добавлять?: \n'))
    filename = input('Напишите имя файла с раширением куда будем сохранять\n')
    fun_gen(quantity, filename)
elif enter == '2':
    quantity = int(input('Какое количество имен будем генерировать?: \n'))
    filename = input('Напишите имя файла с раширением куда будем сохранять:\n')
    func_name(quantity, filename)
elif enter == '3':
    file1 = input('Введите имя файла с числами\n')
    file2 = input('Введите имя файла с именами\n')
    func_sum(file1, file2)
elif enter == '4':
    endfile = input('Введите окончание файла\n') 
    extension = input('Файлы с каким расширением будем переименовывать?\n')
    diap = list((input('Какой дипазон будем оставлять от прежнего имени, введите бе пробелов?\n')))
    koldigit = input('Какое кол-во цифр будет перед нумеровкой?')
    extend = input('Введите желаемое расщирение переименованного файла\n')
    rename(endfile, extension, diap, koldigit, extend)
elif enter == '5':
    extension = input('Какое расширение будет у файлов?\n')
    fun_create(extension)
elif enter == '6':
    quantity = int(input('С каким количеством расширений будем создавать файлы?\n'))
    my_dict = {}
    count = 1
    os.path.exists('my_folder')
    for i in range(quantity):
        extension = input(f'Введите {count} расширение:\n')
        copy_file = input(f'Какое количество файлов будем делать с расширением {extension}:\n')
        my_dict[copy_file] = extension
        count +=1
    create_file(my_dict)
elif enter == '7':
    
    fun_sort()
    
    

else: print('Такой функции нет')


