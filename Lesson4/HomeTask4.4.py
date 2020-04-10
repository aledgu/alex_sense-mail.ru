my_list = input('Введите список чисел через пробел: ').split()
result_List = [int(i) for i in my_list if my_list.count(i) == 1]
print(result_List)