import dump_exec_aux as aux
import database as db
import logging
from datetime import datetime

#Tirado de https://docs.python.org/3/howto/logging-cookbook.html
# create logger with 'spam_application'
logger = logging.getLogger('MainExtractor')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('logs\\logging_file_{}.log'.format(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("*************************************************")
logger.info("Iniciando operação em {}".format(datetime.now()))
logger.info("*************************************************")

error = True

db.setup()

error = aux.dump_uasgs() and error
error = aux.dump_licitacoes() and error
error = aux.dump_modalidades_licitacoes() and error
error = aux.dump_orgaos() and error


print("\n\n")
if(error):
	print("Tudo correu bem. Todas as operações feitas podem ser consultadas no log.")
else:
	print("Ocorreu algum error. Por favor, cheque o ultimo log gerado.")
print("\n\n")

logger.info("*************************************************")
logger.info("Terminou operação em {}".format(datetime.now()))
logger.info("*************************************************")