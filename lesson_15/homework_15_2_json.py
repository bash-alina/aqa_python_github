'''Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу
виведіть через логер на рівні еррор у файл json__<your_second_name>.log'''

import json
from pathlib import Path # стандарт - для того аби працювати з папками
import logging

parent_dir = Path(__file__).parent /'json' #шлях до папки json
files = [f for f in parent_dir.iterdir() if f.is_file()]  # Отримання списку всіх файлів

logging.basicConfig( # Налаштовує кореневий логер писати у файл
        filename='json_homework_15_2.log',
        level=logging.INFO, # Базовий рівень, щоб бачити INFO, WARNING, ERROR
        format= '%(asctime)s - %(levelname)s - %(message)s',
        force=True
        )
logger = logging.getLogger("log_event") # функція logging.getLogger

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        try: # блок try, який перехоплює помилки
            data_ = json.load(file)
        except json.decoder.JSONDecodeError as e: # якщо файл невалідний
            logger.error(f'{f.name} not valid json via {e}')


