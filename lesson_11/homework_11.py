#"""Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
#[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
#Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
#Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
#Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
#Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”"""


#def calculate_sum(one_string): # calculate_sum: дала назву своїй функції def ("define"),(one_string) - параметр/аргумент функції
##Я кажу системі - отримати частину даних(one_string), (one_string) - зміна, наприклад (one_string) = "1,2,3,4"...
#    general_sum = 0
#    parts = one_string.split(",") #розділяю на частини масив по комам - в мене буде 3 частини. Важливо аргумент функції передати тут же - one_string
## split - це метод для рядків, який розділяє рядок. Я кажу йому - розділяй по комі, тобто кожен мій рядок буде розділений по комі. (one_string) для ”1,2,3,4” - це 4 шматочки, які будуть розділені
#    for part in parts: # внутрішній цикл for, аби обробити кожен отриманий шматочок, який був розділений комою. Part - я можу назвати як завгодно, тут важливо використати правильну назву масиву,яку вказала вище parts
#        try: # використовую цю команду для обробки помилок. Наби я кажу спробуй виконати код, але може бути помилка. Try завжди працює разом з except
#            number = int(part) # int() вбудована функція, яка перетворює рядок у ціле число. Як система дійде до qwerty1 - то це буде в моєму випадку ValueError
#            general_sum += number # general_sum = general_sum + number. Оператор додавання. В нашому випадку порахує тільки дві стрінги, адеж треття qwerty1 - це ValueError
#        except ValueError: # якщо в коді помилка (ValueError) система звертається до except. Так ми не завалюємо код, а йдемо далі.
#            return "Error: the system can't calculate the sum" # В моєму випадку поверне через qwerty1 - бо це  ValueError
#            # return обов'язковий в except, print тут використовувати не можна, бо має перестати рахувати і повренути текст "Error: the system can't calculate the sum". А print - просто друкує
#    return str(general_sum) # return - завершує функцію. Потрібна для того, аби вивести правильне обчислення - 10 та 60, повертає в стрінгу, бо в нас текст помилки - це теж стрінга.
#    без return str(general_sum) буде None для "1,2,3,4" та "1,2,3,4,50"
#
#array_with_strings = [
#    "1,2,3,4",
#    "1,2,3,4,50",
#    "qwerty1,2,3",
#]
#
#print("Result:")
#for every_string in array_with_strings: # зовнішній цикл для обробки загального масиву даних array_with_strings. Я кажу системі оброби кожну список. Нагадую every_string - можу назвати як хочу, важлива тут вказати правильну назву для array_with_strings
#    finally_result = calculate_sum(every_string) # Ось тут я викликаю функцію, яку написала вище і рахую кожний з 3 списків в array_with_strings
#    print(finally_result) # виводжу отриманий результат

def calculate_sum(one_string):
    general_sum = 0
    parts = one_string.split(",")
    for part in parts:
        try:
            number = int(part)
            general_sum += number
        except ValueError:
            return "Error: the system can't calculate the sum"
    return str(general_sum)

array_with_strings = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3",
]

print("Result:")
for every_string in array_with_strings:
    finally_result = calculate_sum(every_string)
    print(finally_result)