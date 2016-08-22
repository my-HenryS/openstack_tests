import logging
import logging.handlers

LOG_FILE = "test.log"

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024) #, backupCounts = 5)

fmt = '%(asctime)s - %(filename)s:%(lineno)s - [%(levelname)s]  - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('test')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.info('second info message')
