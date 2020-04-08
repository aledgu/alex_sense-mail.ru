result = 0
while True:
    num_lust = input('Введите последовательность чисел через пробел: ').split()
    for i in range(0, len(num_lust), 2):
        b = int(num_lust[i]) + int(num_lust[i+1])
        result += + b
    print(result)
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
print(result)