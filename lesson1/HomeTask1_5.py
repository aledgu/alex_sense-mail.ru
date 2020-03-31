revenue = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))

if revenue > cost:
    profit = int(((revenue - cost)/revenue)*100)
    print(f'Ваша рентабельность составила {profit}%')
    officer = int(input('Введите количество сотрудников: '))
    profit_to_one_officer = int((revenue - cost)/officer)
    print(f'Прибыль на одного сотрудника равна {profit_to_one_officer}')
elif revenue == cost:
    print('Вы работаете в 0')
else:
    loss = cost - revenue
    print(f'Вы работаете в - ваш убыток {loss}')