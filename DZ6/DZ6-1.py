# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

# def date(date):
#     test_data = date.split('.')
#     if int(test_data[0]) > 31:
#         return False
#     elif int(test_data[1]) > 12:
#         return False
#     elif int(test_data[0]) > 9999:
#         return False
#     else: return True

# print(date('12.05.2023'))

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

def date(date):
    test_data = date.split('.')
    if int(test_data[0]) > 31:
        return False
    elif int(test_data[1]) > 12:
        return False
    elif int(test_data[0]) > 9999:
        return False
    else: return True

print(date(str(argv)))