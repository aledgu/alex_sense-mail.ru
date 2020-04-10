full_time = int(input('Введите выработку в часах: '))
pay_rate = int(input('Ставка в час: '))

try: bonus = int(input('Введите сумму бонуса: '))
except ValueError:
    bonus = 0


def earnings(full_time, pray_rate, bonus=0):
    earn = ((full_time*pray_rate)+bonus)
    print('Зарплата сотрудника = ', earn)

earnings(full_time, pay_rate, bonus)