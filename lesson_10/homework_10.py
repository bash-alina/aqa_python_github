# Task_01
"""Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Клас TeamLead повинен мати всі атрибути як
Manager (ім'я, зарплата, відділ), Developer(ім'я, зарплата, мова програмування),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівни"""
import math


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

# OR - тут підказали
# class Employee:
#     def __init__(self, name, salary, **kwargs):
#         self.name = name
#         self.salary = salary
#      # super().__init__(**kwargs) - як я зрозуміла можна його не викликати, бо Employee останнім в ланцюжку
#
# class Manager(Employee):
#     def __init__(self, name, salary, department, **kwargs):
#         super().__init__(name, salary, **kwargs)
#         self.department = department
#
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language, **kwargs):
#         super().__init__(name, salary, **kwargs)
#         self.programming_language = programming_language
#
# class TeamLead(Manager, Developer):
#     def __init__(self, name, salary, department, programming_language, team_size):
#         super().__init__(name, salary, department=department, programming_language=programming_language)
#         self.team_size = team_size

# Task_02
"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    # Створіть абстрактний клас "Фігура
    @abstractmethod
    def get_area(self): # для отримання площі
        pass

    @abstractmethod
    def get_perimeter(self): # для отримання периметру
        pass

# перша фігура - (> 2)
class Rhombus(Figure):
    def __init__(self, side_a, angle_a):
        self.__side_a = side_a
        self.__angle_a = angle_a

        if not (0 < angle_a < 180):
            raise ValueError("Angle should be between 0 and 180")

    def get_area(self):
        angle_rad = math.radians(self.__angle_a)
        return (self.__side_a ** 2) * math.sin(angle_rad)
    def get_perimeter(self):
        return 4 * self.__side_a

# друга фігура - (> 2)
class Square(Figure):
    def __init__(self, side_a):
        self.__side_a = side_a

    def get_area(self):
        return self.__side_a ** 2
    def get_perimeter(self):
        return 4 * self.__side_a

# третя фігура - (> 2)
class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def get_area(self):
        return self.__side_a * self.__side_b
    def get_perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

objects = [
    Rhombus(side_a=10, angle_a= 60),
    Square(side_a=10),
    Rectangle(side_a=5, side_b=10),
]

# у циклі порахуйте та виведіть в консоль площу та периметр кожної
print("Getting area and perimeter")
for i, item in enumerate(objects):
    area = item.get_area()
    perimeter = item.get_perimeter()
    figure_type = type(item).__name__

    print(f"Figure ({figure_type}):")
    print(f"Area:  {area}")
    print(f"Perimeter: {perimeter}")



