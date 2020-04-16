"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
 {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""
class Worker:
    def __init__(self, wage=0, bonus=0):
        self.name = 'name'
        self.worker_surname = "surname"
        self.worker_position = "position"
        self._worker_income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Полое имя сторудника {self.worker_surname, self.name}')

    def get_total_income(self):
        print(self._worker_income["wage"] + self._worker_income["bonus"])
new_worker = Position(150, 150)
new_worker.name = 'Alex'
new_worker.worker_surname = 'Gro'
new_worker.worker_position = 'fantazer'
new_worker.get_full_name()
new_worker.get_total_income()
