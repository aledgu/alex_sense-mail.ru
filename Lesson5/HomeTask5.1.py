my_list = input('Введите данные для записи в файл, для окончания нажмите Enter: ')
while my_list != '':
    with open('Файл с дозаписью с новой строки.txt', 'a+') as f:
        f.write(my_list)
        f.write('\n')

    my_list = input('Введите данные для записи в файл, для окончания нажмите Enter: ')