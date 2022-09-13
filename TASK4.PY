""" 
## 4 - Реализуйте выдачу случайного числа
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
Учтите, что есть диапазон: от(минимальное) и до (максимальное)
Домашнее задание отправляйте в виде ссылки на гит-репозиторий
 """
import datetime
min = float(input('Введите минимальное число для генерации случайного: '))
max = float(input('Введите максимальное число для генерации случайного: '))
if min > max:
    print ('Введенное Вами минимальное больше максимального, меняем их местами')
    temp_value = min
    min = max
    max = temp_value
while True:
    dt = datetime.datetime.now()
    dt1 = datetime.datetime.now()
    dt2 = datetime.datetime.now()
    dt3 = datetime.datetime.now()
    newrandom = round((dt.microsecond * dt2.microsecond + dt3.microsecond)% (dt1.microsecond/1000),7)
    if min < newrandom < max:
        break
print(newrandom)