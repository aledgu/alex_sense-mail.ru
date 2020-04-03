nut_number = [7, 5, 3, 3, 2]

num = int(input('Vvedite chislo: '))

if nut_number.count(num) != 0:
    nut_number.insert(nut_number.index(num), num)
    print(nut_number)
elif num > int(nut_number[0]):
    nut_number.insert(0, num)
    print(nut_number)
else:
    nut_number.append(num)
    print(nut_number)