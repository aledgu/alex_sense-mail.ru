import random

rand_list = (random.choices([i for i in range(1, 100)], k = 4))
with open('FFt 5.5.txt', 'w', encoding='UTF-8') as new_file:
    for i, el in enumerate(rand_list):
        new_file.write(str(el))
        if i == len(rand_list) - 1:
            res = sum(rand_list)
            new_file.write(f'. Сумма всех чисел равна {res}')
            break
        new_file.write(', ')

print(res)