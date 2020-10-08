# Задание3: Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(number):
       return sum(number)
a = int(input('Введите a= '))
b = int(input('Введите b= '))
c = int(input('Введите c= '))
numbers = [a, b, c]
number = sorted(numbers, reverse=True)[:2]
print(my_func(number))