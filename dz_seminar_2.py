# Задача 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input("введите число: ")
# s = 0
# for i in n:
#         if i.isdigit():
#                 s+=int(i)
# print(s)


# Задача 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# m = []
# f = 1
# for i in range(1,n+1):
#         f*=i
#         m.append(f)
# print(m)


# Задача 3.
# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input("Введите число: "))
# m = {}
# s = 0
# for i in range(1,n+1):
#         m[i] = round((1+1/i)**i,2)
#         s+=m[i]
# print(m)
# print(s)


# Задача 4.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.







