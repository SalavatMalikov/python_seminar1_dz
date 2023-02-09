#Задача 1.Найдите количество вхождений числа k в список list_1. 
# Результат запишите в переменную res. Выводить переменную res на экран не требуется.

# list_1 = [1, 2, 3, 3, 4, 5]
# k = 3
# res = 0
# for i in list_1:
#     if i==k:
#         res+=1
# print(res)

#Задача 2
# Найдите в list_1 ближайший по величине к числу k элемент. 
# Сохраните этот элемент в переменную res. 
# Выводить переменную res на экран не требуется.

# list_1 = [1, 2, 3, 3, 4, 6]
# k = int(input("Введите число"))
# min = abs(k - list_1[0])
# res = list_1[0]
# for i in range(len(list_1)):
#     if min>abs(k-list_1[i]):
#         min = abs(k-list_1[i])
#         res = list_1[i]
# print(res)


#Задача 3. Скрабл

word = input("введите слово: ")
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = word.upper()  
res = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                print(j)
                res = res + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                res = res + j
print(res)


