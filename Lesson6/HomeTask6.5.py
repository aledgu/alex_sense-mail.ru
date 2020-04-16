
class Stationery:
    def __init__(self, title):
        self.stat_title = title
    def draw(self): print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self): print('Уже не запуск отрисовки.')

class Pencil(Stationery):
    def draw(self): print('Карандаш даром даш?')

class Handle(Stationery):
    def draw(self): print('Маркером по лицу.')

sel = Stationery('skrepka')
sel.draw()
my_pen = Pen('arabskaya noch')
my_pen.draw()
my_pencil = Pencil('Ne tvoya')
my_pencil.draw()
my_handel = Handle('Vot eto da')
my_handel.draw()