"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h
    def get_sq_coat(self):
        return round(self.v / 6.5 + 0.5)

    def get_sq_jacket(self):
        return round(self.h * 2 + 0.3)

    @property
    def all_sq(self):
        return round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3))

class Coat(Clothes):
    @property
    def get_sq_coat(self):
        return round(self.v / 6.5 + 0.5)


class Jacket(Clothes):
    @property
    def get_sq_jacket(self):
        return round(self.h * 2 + 0.3)


svit = Clothes(2 , 1)
jacket = Jacket(1, 6)
print(jacket.get_sq_jacket)