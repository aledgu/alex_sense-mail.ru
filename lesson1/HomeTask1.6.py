first_day = int(input('Сколько километров спортсмен пробежал в первый день: '))
full_distans = int(input('Общая дистанция, которую спортсмен должен пробежать: '))
day = 1
while full_distans > first_day:
    first_day *= 1.1
    day += 1
day = int(day)
print(f'Спортсмен достигнет результата через {day} дней')