# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('second.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'Колличество строк : {len(lines)}')
    for line in lines:
        res = len(line.split())
        print(f'Колличество слов : {res}')
