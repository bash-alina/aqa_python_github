"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""

class Rhombus: # Створіть клас геометричної фігури "Ромб"
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        #self.angle_b = 180 - angle_a

        #if self.angle_a + self.angle_b != 180: # Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
           # print("Error: The sum of angles is not equal 180")

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value > 0: # Значення сторони сторона_а повинно бути більше 0
                super().__setattr__(name, value)
            else:
                print("Error: side_a is less than zero ")
        elif name == 'angle_a':
            if 0 < value < 180:
                super().__setattr__("angle_a", value)
                angel_b_value = 180 - value # значення кут_б обчислюється автоматично.
                super().__setattr__("angle_b", angel_b_value)
            else:
                print(f"Error: {name} should be between 0 and 180 ")
        elif name == 'angle_b': # not manual updating
            print("Error: angle_b should calculate automatically from angle_a")
            return
        else:
            super().__setattr__(name, value)

#rhombus_1 = Rhombus(side_a=10, angle_a=20)
#print(f"Rhombus 1: a={rhombus_1.side_a}, A={rhombus_1.angle_a}°, B={rhombus_1.angle_b}°")
#rhombus_1.angle_a = 45
#print(f"Rhombus update: a={rhombus_1.side_a}, A={rhombus_1.angle_a}°, B={rhombus_1.angle_b}°")
#rhombus_1.side_a = 0
#print(f"Rhombus error: a={rhombus_1.side_a}, A={rhombus_1.angle_a}°, B={rhombus_1.angle_b}°")
#rhombus_1.angle_b = 90
#print(f"Rhombus error with angle_b: A={rhombus_1.angle_a}°, B={rhombus_1.angle_b}°")


