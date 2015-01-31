from logging import getLogger, FileHandler, Formatter, INFO, DEBUG

logger = getLogger(__name__) # this will show current module in the log line
logger.setLevel(INFO)

# create a file handler

handler = FileHandler('hello.log')
handler.setLevel(INFO)

# create a logging format

formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

logger.info('Happy logging!')
