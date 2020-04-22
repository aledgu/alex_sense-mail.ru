import random

class LotoCard:
    def __init__(self, player_name):
        self.player = player_name

    def get_card(self):
        lot_ticket = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        number_list = [i for i in range(1, 91)]
        for l in range(0, (len(lot_ticket))):
            del_numb = random.sample(number_list, 5)
            del_numb.sort()
            poz = random.sample([i for i in range(0, 9)], 5)
            poz.sort()
            for i, el in enumerate(poz):
                lot_ticket[l].pop(el)
                lot_ticket[l].insert(el, del_numb[i])
                number_list.remove(del_numb[i])
        return lot_ticket

class LotoGame(LotoCard):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        self.player1 = self.get_card()
        self.player2 = self.get_card()
        number_list = [i for i in range(1, 91)]
        stop_game = int(input('Введите количество ходов, которые будете играть. От 0 до 90 включительно:'))
        log = 'Первый ход'
        for number in number_list:
            user_list = []
            for i in self.player1:
                for j in i:
                    if j != ' ': user_list.append(j)
                    if 'X' in user_list: user_list.remove('X')
            computer_list = []
            for i in self.player2:
                for j in i:
                    if j != ' ': computer_list.append(j)
                    if 'X' in computer_list: computer_list.remove('X')
            # b = 10
            b = random.choice(number_list)
            number_list.remove(b)
            print(f'{log}:')
            log = 'Следующий ход'
            if number+1 == stop_game:
                log = 'Последний ход'
            print('Из мешка выпал бочонок номер:', b, '\n', 'Карточка пользовалетя:\n', '-'*25, '\n',
                  str('\n'.join([' '.join([str(j) for j in i]) for i in self.player1])), '\n', '-'*25)
            print('Карточка компьютера:\n', '-'*25, '\n', str('\n'.join([' '.join([str(j) for j in i]) for i in self.player2])),'\n', '-'*25)

            if b in computer_list:
                computer_list.remove(b)
                for l in range(0, (len(self.player2))):
                    if b in self.player2[l]:
                        ind = self.player2[l].index(b)
                        self.player2[l].remove(b)
                        self.player2[l].insert(ind, 'X')

            user_move = input('Ход пользователя. Выберите действие из списка: "зачеркнуть" или "продолжить":').lower()
            if b in user_list and user_move == 'зачеркнуть':
                print("Отлично! стираем выпавший бочонок! Идем дальше...")
                user_list.remove(b)
                for l in range(0, (len(self.player1))):
                    if b in self.player1[l]:
                        ind = self.player1[l].index(b)
                        self.player1[l].remove(b)
                        self.player1[l].insert(ind, 'X')
            elif b not in user_list and user_move == 'продолжить':
                print('Отлично! Идем дальше...')
            else:
                print('Сожалею, но вы сделали неправильный ход и проиграли!')
                break
            if number+1 > stop_game:
                print('Ходы закончились. Ходов больше нет')
                if len(computer_list) < len(user_list):
                    print('В этот раз компьютеру повезло больше чем вам. Не переживайте в следующий раз вам обязательно фортанет!\n',
                          '-'*25, '\n', str('\n'.join([' '.join([str(j) for j in i]) for i in self.player2])),'\n', '-'*25)
                elif len(computer_list) > len(user_list):
                    print('Поздравляю с победой!\n', '-'*25, '\n',
                          str('\n'.join([' '.join([str(j) for j in i]) for i in self.player1])), '\n', '-'*25)
                else:
                    print('Сегодняшняя битва закончилась ничьей!')
                break


human = LotoCard('ivan')
computer = LotoCard('zlodei')
game = LotoGame(human, computer)
game.start()