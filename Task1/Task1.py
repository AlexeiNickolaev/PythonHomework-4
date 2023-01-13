# Вычислить число c заданной точностью d
import math
p=math.pi
d=input('Задайте d для точности вывода числа пи (пример: 0.001): ')
count=0
d=d.replace('0.', '')
for i in d:
    count+=1
print(f'число {p:.{count}f}') 