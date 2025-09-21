from operator import index

adwentures_of_tom_sawer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")

print(adwentures_of_tom_sawer)

# ----------------------------------------------------------------------------------------
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_1 = adwentures_of_tom_sawer.count("h")
print(count_1)
count_2 = adwentures_of_tom_sawer.count("H")
print(count_2)
total_count = adwentures_of_tom_sawer.count("h") + adwentures_of_tom_sawer.count("H")
print(total_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
#count = adwentures_of_tom_sawer.count{uper()}
#print(count)
#count = adwentures_of_tom_sawer.upper().count
#index = adwentures_of_tom_sawer.find(upper(), [0:])
#upper_case = adwentures_of_tom_sawer.isupper()
#if "letter.isupper()" in adwentures_of_tom_sawer.upper():
#    print(adwentures_of_tom_sawer)
#search_upper_case = adwentures_of_tom_sawer
#index = adwentures_of_tom_sawer.find(letter.isupper())
#print(adwentures_of_tom_sawer[index:])
show_letter_upper_case = [letter for letter in adwentures_of_tom_sawer if letter.isupper()]
print(f'show_letter_upper_case = {show_letter_upper_case}')
count_letter_upper_case_1 = len(show_letter_upper_case)
print(count_letter_upper_case_1)

#count_letter_upper_case = sum(1 for letter in adwentures_of_tom_sawer if letter.isupper()) - цю ідею подав gbt :(
#print(count_letter_upper_case)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
search_phrase_1 = "Tom"
index_1 = adwentures_of_tom_sawer.find(search_phrase_1)
#index_2 = adwentures_of_tom_sawer.find(search_phrase_1, index_1 + 1)
#print(adwentures_of_tom_sawer[index_2:])

if index_1 != -1:
   index_2 = adwentures_of_tom_sawer.find(search_phrase_1, index_1 + 1)
#   print(index_2)
   print(adwentures_of_tom_sawer[index_2:])
else:
     print('error: not found')



# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""


# task 09 #Done
""" Перевірте чи починається якесь речення з "By the time".
"""
search_phrase = "By the time"
index = adwentures_of_tom_sawer.find(search_phrase)
if index != -1:
    print('True')
else:
    print('False')

# task 10 - ДОРОБИТИ
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
row = ('And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, '
       'Tom was literally rolling in wealth.')
print(f'Count words = {len(row.split())}')

# OR

last_sentence = adwentures_of_tom_sawer.split('.')[-1]
print(last_sentence)