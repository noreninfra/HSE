class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def up(self, amount):
        self.salary += amount

    def print_(self):
        print(f"Сотрудник {self.name}, зарплата {self.salary}")


ivan = Employee("Иван", 1000)
ivan.up(300)
ivan.print_()
