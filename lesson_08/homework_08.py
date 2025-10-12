"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""
class Student:
    def __init__(self, name, last_name, age, average_score ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def get_average_score(self):
        return self.average_score

    def set_average_score(self, value):
        if isinstance(value, (int)):
            self.average_score = value
        else:
            print("Type isn't correct: waiting for int")

student_1 = Student(name="Alina", last_name="Bashlykova", age=37, average_score=80)
print("Full information about Student:", student_1.name, student_1.last_name, student_1.age, student_1.average_score)

student_1.set_average_score(90)
print("New full information about Student:", student_1.name, student_1.last_name, student_1.age, student_1.average_score)
print("New average score of Student:", student_1.average_score)
