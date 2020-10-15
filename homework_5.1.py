# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('first.txt', 'w', encoding='utf-8') as file:
    file.writelines(input('ВВести: \n'))
    while True:
        f = input()
        if f == '':
            break
        file.write(f + '\n')