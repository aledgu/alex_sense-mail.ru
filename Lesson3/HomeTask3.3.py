def my_func ():
    spisok = []
    for i in range(3):
        spisok.append(int(input('Vvedite chilso: ')))
        spisok.sort()
    print(spisok[2] + spisok[1])
my_func()