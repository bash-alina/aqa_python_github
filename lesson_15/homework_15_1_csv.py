# НЕ РОЗІБРАЛАСЬ!
# 1. Створити список файлів, які будуть оброблятись
import csv
from pathlib import Path # стандарт
from collections import OrderedDict # cтандартна бібліотека

parent_dir = Path(__file__).parent /'csv' #шлях до папки csv
files = [f for f in parent_dir.iterdir() if f.is_file()]  # Отримання списку всіх файлів
#for f in files:
#    print(f.name)

# 2. Написати функцію, яка буде брати файл - видаляти дублі та записувати у файл вже без дублів

def parse(data): # функція, яка зберігає унікальність рядків
    result = OrderedDict() # зберігаємо правильний порядок. Це класс OrderedDict()
    for row in data: #лист даних, по якому ми проходимось
        id, *data = map(str.strip, row) # str.strip - це функція, map - теж функція. map виконає str.strip для кожного row
        if id not in result: # перевірямо, що немає
            result[id] = data
    return result

def remove_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as f: # відкриває і закриває файл - на читання 'r'
        new_data = csv.reader(f) # записати прочитані дані (з файлу) в зміну
        return parse(new_data)

def write_to_file(file_name, lines):
    with open(file_name, 'a', encoding='utf-8') as f: # 'a' - append - дописую файл
        writer = csv.writer(f) # створили об'єкт, який буде писати в файл
        for l in lines.values(): # поверне значення
            writer.writerow(l)  # записує всі значення в строку

new_file = parent_dir/'result_homework_15_1.csv'
for file in files: # створюю новий файл
    result = remove_duplicates(file)
    write_to_file(new_file, result)


# Не вийшло
#def remove_duplicates(file_path):
#    with open(file_path, 'r', encoding='utf-8') as f: # відкриває і закриває файл - на читання 'r'
#        lines = f.readlines() # вичитує
# #       lines = [] # з ітератору - робимо список
# #       for l in reader:
# #           lines.append(', '.join(l))
#       # result = set(lines) # вносимо всі lines в set{}
#        # lines = [f for f in reader]
#        return set(lines) # вносимо всі lines в set{}
#
#def write_to_file(file_name, lines):
#    new_lines = []
#    for l in lines:
#        new_lines.append(', '.split(l))
#    with open(file_name, 'a', encoding='utf-8') as f: # 'a' - append - дописую файл
#        writer = csv.writer(f) # створили об'єкт, який буде писати в файл
#        writer.writerow(lines) # записує всі строки в файл
#
#new_file = parent_dir/'result_homework_15_1.csv'
#for file in files: # створюю новий файл
#    result = remove_duplicates(file)
#    write_to_file(new_file, result)

