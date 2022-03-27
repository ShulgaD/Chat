import os
import logging
from pathlib import Path

p = Path(__file__).parents[1]
p = os.path.join(p, 'logs\client.log')


FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s ")
FILE_HANDLER = logging.FileHandler(p, encoding='utf-8')
FILE_HANDLER.setFormatter(FORMATTER)

LOG = logging.getLogger('client')
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
