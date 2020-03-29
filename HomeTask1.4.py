p = int(input('Введите число: '))
m = p % 10
p = p // 10
while p > 0:
    if p % 10 > m:
        m = p % 10
    p = p // 10
print(m)