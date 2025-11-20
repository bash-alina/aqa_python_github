'''Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо'''

import logging
import xml.etree.ElementTree as ET

logging.basicConfig( # Налаштовує кореневий логер писати у файл
        filename='xml_homework_15_3.log',
        level=logging.INFO, # Базовий рівень, щоб бачити INFO, WARNING, ERROR
        format= '%(asctime)s - %(levelname)s - %(message)s',
        force=True
        )
logger = logging.getLogger("log_event") # функція logging.getLogger

tree = ET.parse('xml/groups.xml')
root = tree.getroot()


for group in root.findall('group'):
    timingExbytes = group.find('timingExbytes')
    if timingExbytes is not None:
        incoming = timingExbytes.find('incoming')
        if incoming is not None:
            logger.info(f'group = {group.find('number').text}, incoming = {incoming.text}')
