from itertools import cycle, count

a = int(input('Введите число начала цикла: '))

for i in count(a):
    print(i)
    if i > 15:
        break
b = input('Введите список символов разделенных пробелом: ').split()

for i in cycle(b):
    print('endness cykle')