# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list1 = [2, 5, 8, 9, 8, 5]
print(list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)