# Задание 2 
# a = list(map(int, input('Введите значения через пробел: ').split()))
# a.sort()
# if a[0] + a[1] > a[2]:
#     if a[0] == a[1] == a[2]:
#         b = 'равноcторонний'
#     elif a[0] == a[1] or a[0] == a[2] or a[2] == a[1]:
#         b = 'равнобедренный'
#     else: b = 'разносторонний'
#     print(f'Это {b} треугольник')
# else: print('Что-то не так')


# # Задача 3
# a = int(input('Введите число от 0 до 100 000: '))
# if a < 0 or a > 100000:
#     print('Число не в диапазоне')
# elif a < 2: 
#     print('Число меньше 2') 
# elif a > 2:
#     for i in range(2, a): 
#         if a % i == 0: 
#             print('Число составное') 
#             break
# else:
#     print('Число простое')

# Задача 4

from random import randint
num = randint(0, 1000)
count = 0
print(num)
while count < 10:
    print(f'У  вас осталось {10 - count} попыток') 
    a = int(input('Введите число от 0 до 1000: '))
    if a == num:
        print('Угадал')
        break   
    else: print('Мимо')
    count +=1




