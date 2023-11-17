import logging

# Треугольник
# logging.basicConfig(filename='my_log1.log', encoding='utf-8', level=logging.ERROR)
# a = list(map(int, input('Введите значения через пробел: ').split()))
# a.sort()
# if a[0] + a[1] > a[2]:
#     if a[0] == a[1] == a[2]:
#         b = 'равноcторонний'
#     elif a[0] == a[1] or a[0] == a[2] or a[2] == a[1]:
#         b = 'равнобедренный'
#     else: b = 'разносторонний'
#     print(f'Это {b} треугольник')
# else: logging.error('Что-то не так')

#Банкомат
logging.basicConfig(filename='my_log2.log', encoding='utf-8', level=logging.INFO)
oper = int
count = 0
cash = 0
count = 1
def withdraw(cash):
    a = int(input('Введите сумму кратную 50 у.е.: '))
    if a % 50 == 0:
        if a < cash:
            cash = cash - a - percent(a)
            print(f'Вы сняли {a}')
            logging.info(f'Клиент снял {a}')
        else: 
            print(f'Не хватает денег на балансе')
            logging.error('не хватает денег на балансе')
    else: 
        print('Сумма не кратна 50 у.е.')
        logging.info('Сумма не кратна 50 у.е.')
    return cash

def refil(cash):
    b = int(input('Какую сумму вы хотите внести?: '))
    cash = cash + b
    print(cash)
    return cash

def percent(a):
    perc = a * 0.015
    print(perc)
    if perc > 30 and perc  < 300:
        return perc
    elif perc < 30:
        return 30
    else: return 300


while oper != 4:
    oper = int(input('Какую операцию хотите совершить?: \n 1. Снять деньги \n 2. Пополнить баланс \n 3. Баланс\n 4.Выйти\n' ))
    if cash > 5000000:
            cash = cash *0.9
    if count % 3 == 0:
        print('остаток от деления', count % 3 )
        cash = cash * 1.03
        print(f'Баланс: {cash}')
    if oper == 1:
        cash = withdraw(cash)
        print(f'Баланс: {cash}')
    if oper == 2:
        cash = refil(cash)
        print(f'Баланс: {cash}')
    if oper == 3:
        print(f'Баланс: {cash}')
    count += 1
