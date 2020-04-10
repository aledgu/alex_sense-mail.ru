# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
my_list = [int(i) for i in input('Введите список чисел через пробел: ').split()]
result_List = [int(el) for i, el in enumerate(my_list) if my_list[i] > my_list[i-1]]
print(result_List)