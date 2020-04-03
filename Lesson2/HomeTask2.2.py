spisok = []
a = input('Вводите символы. Для завершения введите end!: ')
while a != 'end':
    spisok += [a]
    a = input('Вводите символы. Для завершения введите end!: ')
print(spisok)
n_s = 0
for f in range(int(len(spisok)/2)):
    spisok[n_s],spisok[n_s+1] = spisok[n_s+1],spisok[n_s]
    n_s += 2

print(spisok)