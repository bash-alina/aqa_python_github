# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
sum_of_even_numbers = 0
for number in list_of_numbers:
    if number % 2 == 0:
        sum_of_even_numbers = sum_of_even_numbers + number

print(sum_of_even_numbers)