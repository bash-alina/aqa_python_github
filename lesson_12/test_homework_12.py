"""Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію."""

import pytest

from lesson_07.homework_07 import sum_of_even_numbers # не забувати додавати папку звідки взяла файл та імпортувати конретну функцію, з якою хочу прауювати. Або можна імпортувати весь файл, з усіма функціями

def test_calculation_of_even_numbers(): # 1. positive test: Перевірити, що повертається сума лише для парних чисел. Непарні числа система ігнорує
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
    expected_result = 1262 # Тут маю прописати результат, якщо пропишу те саме, що в actual_result, то це буде дублювати assert
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result # просто запам'ятат синтаксис

def test_zero_is_even_number(): # 2. negative test: Перевірити, що повертається сума лише для парних чисел, де 0 теж парне число
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
    expected_result = 1262
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_of_negative_numbers(): # 3. negative test: Перевірити, що система поврене значення для негативних чисел
    list_of_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -20, -25, -199, -1212]
    expected_result = -1262
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_sum_is_negative_when_mixed(): # 4. negative test: Перевірити, що система поврене значення розрахувавши правильно позитивні та негативні числа, де більше негативних чисел
    list_of_numbers = [-1, 2, -3, -4, -5, -6, -7, -8, -9, 10, -20, -25, -199, -1212]
    expected_result = -1238
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_sum_is_positive_when_mixed(): # 5. negative test: Перевірити, що система поврене значення розрахувавши правильно позитивні та негативні числа, де більше позитивних чисел
    list_of_numbers = [-1, 2, 3, 4, 5, -6, -7, 8, -9, 10, 20, -25, -199, 1212]
    expected_result = 1250
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_of_large_even_and_odd_numbers(): # 6. negative test: Перевірити, що система поврене значення опрацювавши великі числа
    large_1 = 99999999999999998
    large_2 = 88888888888888888
    large_3 = 99999999999999999
    list_of_numbers = [large_1, large_2, large_3]
    expected_result = large_1 + large_2
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_only_odd_numbers(): # 7. negative test: Перевірити, що повертається 0, якщо у списку лише непарні числа
    list_of_numbers = [3, 5, 7, 9, 11, 13, 15, 17, 19]
    expected_result = 0
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_list_without_data(): # 8. negative test: Перевірити, що повертається 0, якщо список порожній
    list_of_numbers = []
    expected_result = 0
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_of_event_numbers_in_string_list(): # 9. negative test: Перевірити, що правильно виконується int(n) - str перетворюється на int
    list_of_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "20", "25", "199", "1212"]
    expected_result = 1262
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

#def test_calculate_list_incorrect_format(): #10 думаю, що тест з TypeError немає сенсу, тому виправила функцію додала try/except - для виводку помилкового значення в тесті. А не як зараз просто ігнорування помилки
#    list_of_numbers = [1, 2, 3, 'r', 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
#    with pytest.raises(TypeError):
#        sum_of_even_numbers(list_of_numbers)

def test_calculation_list_with_incorrect_format(): # 10. negative test: Перевірити, що система поверне помилку для рядка з некоректиним символом
    list_of_numbers = [1, 2, 3, 'r', 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
    expected_result = "Error: list has incorrect symbols"
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_list_with_space(): # 11. negative test: Перевірити, що система поверне помилку через пробіл у спсику
    list_of_numbers = [1, 2, 3, 4, " ", 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
    expected_result = "Error: list has incorrect symbols"
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result

def test_calculation_list_with_float(): # 12. negative test: Перевірити, що система поверне помилку  через дріб у списку
    list_of_numbers = [1, 2, 3, 4, "2.88", 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
    expected_result = "Error: list has incorrect symbols"
    actual_result = sum_of_even_numbers(list_of_numbers)
    assert expected_result == actual_result









