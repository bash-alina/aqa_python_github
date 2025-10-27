# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2 #DONE_02
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers():
    a = int(2) #   a = int(input("Enter first number: "))
    b = int(3) #   b = int(input("Enter second number: "))
    return a + b

print("Sum of two numbers:", sum_of_numbers())

# task 3 #DONE_03
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list_of_numbers(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Нічого, що тут я використовую нейм зміної таку саму, яку задала при визначенні функціїї ?
print("Average of numbers:", average_of_list_of_numbers(list_of_numbers))

# task 4 #DONE_04
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_row(variable):
    res=''.join(reversed(variable))
    return res

row = reversed_row('Spring is green.') # row = reversed_row(input())
print('Reversed row:', row)

# task 5 #DONE_05
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_in_the_list(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

list_of_words = ["Hi", "Hello", "How"]
print('longest_word:', longest_word_in_the_list(list_of_words))

# task 6 #DONE_06
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 #DONE_07
# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі
#list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
#sum_of_even_numbers = 0
#for number in list_of_numbers:
#    if number % 2 == 0:
#        sum_of_even_numbers = sum_of_even_numbers + number
#
#print(sum_of_even_numbers)

# def sum_of_even_numbers(list_of_numbers):
#    sum_of_even_numbers = 0
#    for number in list_of_numbers:
#        if number % 2 == 0:
#            sum_of_even_numbers = sum_of_even_numbers + number
#    return sum_of_even_numbers

def sum_of_even_numbers(list_of_numbers):
    sum_of_even_numbers = 0
    for n in list_of_numbers:
        try:
            number = int(n)
            if number % 2 == 0:
                sum_of_even_numbers = sum_of_even_numbers + number
        except ValueError:
            return "Error: list has incorrect symbols"

    return sum_of_even_numbers

list_of_numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
print("Sum of even numbers:", (sum_of_even_numbers(list_of_numbers_1)))

# or - але це вже не моя ідея
def sum_of_even_number_another(numbers):
    return sum(number for number in numbers if number % 2 == 0)

list_of_numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 199, 1212]
print("Sum of even numbers another:", sum_of_even_number_another(list_of_numbers_2))

# task 8 #DONE_08
#text = ("Add")
#uniq_symbols = set(text)
#if len(uniq_symbols) > 10:
#    print('True')
#else:
#    print('False')

def count_uniq_symbols_in_the_row(symbols):
    uniq_symbols = set(symbols)
    if len(uniq_symbols) > 10:
        return True
    else:
        return False

text_1 = ("The most widely performed love story")
text_2 = ("Add")
print('True:', count_uniq_symbols_in_the_row(text_1))
print('False:', count_uniq_symbols_in_the_row(text_2))

# task 9 #DONE_09
#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-
#ське моря разом?
#
#BlackSea_area_km2 = 436402
#AzovSea_area_km2 = 37800
#Total_km2 = BlackSea_area_km2 + AzovSea_area_km2
#print(f'{Total_km2 = } km²')

def total_km2(a,b):
    km2 = a + b
    return km2

print("Sum of two numbers:", total_km2(436402,37800))

# task 10 #DONE_10
#Перевірте чи починається якесь речення з "By the time".
#
#search_phrase = "By the time"
#index = adwentures_of_tom_sawer.find(search_phrase)
#if index != -1:
#    print('True')
#else:
#    print('False')

def search_phrase(text,phrase):
    index = text.find(phrase)
    if index != -1:
        return True
    else:
        return False

phrase = "By the time"
text_3 = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print("Search phrase:", search_phrase(text_3, phrase))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""