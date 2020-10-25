class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = [
            {'Director': {'Wage': 150000, 'Bonus': 30000}},
            {'Manager': {'Wage': 80000, 'Bonus': 20000}},
            {'Fitter': {'Wage': 50000, 'Bonus': 10000}}
        ]


class Position(Worker):
    def get_full_name(self):
        return f'Workers full name is {self.name} {self.surname}.'

    def get_total_income(self):
        for pos in self._income:
            if self.position in pos:
                for salary in pos.values():
                    return f"The worker total income in {self.position} position" \
                           f" - {salary.get('Wage') + salary.get('Bonus')}."
        return "There is no such position!"


a = Position(input('Enter Worker name: ').title(),
             input('Enter Worker surname: ').title(),
             input('Enter Worker position(Director, Manager or Fitter): ').title())
print(a.get_full_name())
print(a.get_total_income())
