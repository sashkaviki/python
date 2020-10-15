# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

fileName = 'numbers.txt'
f = open(fileName, 'w', encoding='utf-8')
first = True
inpStr = ''
outStr = ''
print('Введите числа (finish для окончания): ')
while inpStr != 'finish':
    inpStr = input('Введите ' + ('первое' if first == True else 'следующее') + ' число:')
    first = False
    if inpStr == 'finish':
        continue
    try:
        num = int(inpStr)
        outStr += ' ' + str(num)
    except:
        print('Неверное число')
f.write(outStr)
f.close()
f = open(fileName, 'r')
numArr = f.read().strip().split(' ')
sum = 0
for num in numArr:
  try:
    sum += int(num)
  except:
    print('Ошибка в формате файла')
print('Сумма чисел в файле: ', sum)
f.close()