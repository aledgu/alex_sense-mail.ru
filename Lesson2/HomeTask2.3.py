month = int(input('Введите номер месяца: '))

winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9,10,11]
if month in winter_list:
    print('Zima')
elif month in spring_list:
    print('Vesna')
elif month in summer_list:
    print('Leto')
else:
    print('Osen')
year_time = {1: 'Zima', 2: 'Zima', 3: 'Vesna', 4: 'Vesna', 5: 'Vesna', 6:'Leto', 7:'Leto', 8: 'Leto',
             9: 'Osen', 10: 'Osen', 11: 'Osen', 12: 'Zima'}
print(year_time.get(month))