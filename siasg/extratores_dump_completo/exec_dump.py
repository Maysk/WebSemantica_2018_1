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
error = aux.dump_irps() and error
error = aux.dump_precos_praticados() and error
error = aux.dump_registros_preco() and error

error = aux.dump_classes() and error
error = aux.dump_grupos() and error
error = aux.dump_pdms() and error
error = aux.dump_materiais() and error


error = aux.dump_secoes_servicos() and error
error = aux.dump_divisoes_servicos() and error
error = aux.dump_grupos_servicos() and error
error = aux.dump_classes_servicos() and error
error = aux.dump_subclasses_servicos() and error
error = aux.dump_servicos() and error


#error = aux.dump_compras_sem_licitacao() and error
#error = aux.dump_itens_compras_sem_licitacao() and error
#TODO rdcs

error = aux.dump_contratos() and error


error = aux.dump_cnaes() and error
error = aux.dump_municipios() and error
error = aux.dump_ramos_negocio() and error
error = aux.dump_portes_empresa() and error
error = aux.dump_linhas_fornecimento() and error
error = aux.dump_fornecedores() and error
error = aux.dump_ocorrencias_fornecedores() and error



print("\n\n")
if(error):
	print("Tudo correu bem. Todas as operações feitas podem ser consultadas no log.")
else:
	print("Ocorreu algum error. Por favor, cheque o ultimo log gerado.")
print("\n\n")

logger.info("*************************************************")
logger.info("Terminou operação em {}".format(datetime.now()))
logger.info("*************************************************")