
with open('FFt 5.3.txt', encoding='UTF-8') as salary_file:
    salary_list = salary_file.readlines()
name_dict = {i.split()[0]: i.split()[1] for i in salary_list if int(i.split()[1]) < 100000}
name_list = [i for i in name_dict.keys()]
average_salary = sum([int(i) for i in name_dict.values()])/int(len(name_dict.values()))

print(f'Следующие сотрудники имеют оклад ниже 100 тысяч рублей {", ".join(name_list)},'
      f' а их средняя зарплата составляет {average_salary} рублей')