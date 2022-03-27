import os
import logging.handlers
from pathlib import Path

p = Path(__file__).parents[1]
p = os.path.join(p, 'logs\server.log')


FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s ")
FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(p, encoding='utf-8', interval=1, when='D')
FILE_HANDLER.setFormatter(FORMATTER)

LOG = logging.getLogger('server')
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
