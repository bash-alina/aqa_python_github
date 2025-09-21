# task 01 == Виправте синтаксичні помилки 
# print("Hello", end = " ")
#    print("world!")

# Implementation: # Done 01
print("Hello, world")

# task 02 == Виправте синтаксичні помилки
# hello = "Hello"
# world = "world"
# if True:
# print(f"{hello} {world}!")

# Implementation: # Done 02
var_1 = "Hello" # True
var_2 = "world" # True
if True:
    print(f"{var_1}, {var_2}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
# for letter in "Hello world!":
#    print(letter)
    
# Implementation: # Done 03
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
# apples = 2
# banana = x

# Implementation: # Done 04
apples = 2
banana = apples * 4
print("apples =", apples)
print("banana =", banana)


# task 05 == виправте назви змінних
# 1_storona = 1
# ?torona_2 = 2
# сторона_3 = 3
# $torona_4 = 4

# Implementation: # Done 05
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4
    

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
# perimetery = ? + ? + ? + ?
# print()

# Implementation: # Done 06
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4
perimeter_figure = side_1 + side_2 + side_3 + side_4
print("perimeter_figure =", perimeter_figure)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

# Implementation: # Done 07
apples = 4
pears = apples + 5
plums = apples - 2
trees = apples + pears + plums
print("trees =", trees)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

# Implementation: # Done 08
temp_air = 0
temp_air_1 = 5
temp_air_2 = temp_air_1 - 10
temp_air_3 = temp_air_2 + 4
print(f"{temp_air_3}°C")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

# Implementation: # Done 09
boys = 24
girls = boys // 2
attendance_boys = boys - 1
attendance_girls = girls - 2
total_children = sum([boys, girls, attendance_boys, attendance_girls])
print("total_children =", total_children)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
# Implementation: # Done 10
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2)/2
total_price = sum([book_1, book_2, book_3])
print(f"{total_price = } grn.")
