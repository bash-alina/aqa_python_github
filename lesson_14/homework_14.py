"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# import os # Додаємо для видалення лог-файлу перед тестами

# НАЛАШТУВАННЯ ЛОГЕРА (Виносимо за межі функції, виконується один раз), бо якщо залишити в середині функції,
# - логер буде налаштований по кожному виклику в середині функції, але GIT/Pytest можуть ігнорувати повторні виклики
# - це може призвести до хаосу, адже кожен тест може мати різні налаштування

LOG_FILE = BASE_DIR /'login_system.log' # створить лог файл
logging.basicConfig( # Налаштовує кореневий логер писати у файл
        filename=LOG_FILE,
        level=logging.INFO, # Базовий рівень, щоб бачити INFO, WARNING, ERROR
        format= '%(asctime)s - %(message)s', # час -текстове повідомленні логу
        force=True
        )
logger = logging.getLogger("log_event") # Створює логер - тут мені НЕ потрібно додлати хендлер - logging.basicConfig(...),
# Python створює і налаштовує кореневий логер (root logger) і автоматично додає до нього хендлер, який пише у вказаний файл (login_system.log).
# Кожен логер, (EX: logger = logging.getLogger("log_event")), за замовчуванням наслідує налаштування та хендлери від кореневого логера.
def log_event(username: str, status: str):
    # Логування події
    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logger.info(log_message) # при виклику повідомлення проходить через логер,
        # а потім піднімається до кореневого логера і записується у файл завдяки хендлеру, доданому basicConfig. Тому вручну хендлер не додаю, лише якщо мены потрыбно було щось виводити додактово - з лекцыъ приклад про Critical
    elif status == "expired":
        logger.warning(log_message)
    else: # для 'failed' та будь-якого іншого невідомого статусу
        logger.error(log_message)


