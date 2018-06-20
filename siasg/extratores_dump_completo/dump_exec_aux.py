import requests
import json 
import os
import database as db
import logging


logger = logging.getLogger("MainExtractor.ExecAux")

def dump_tabela(url_entidade, elemento_json, nome_da_tabela, atributos_validos):
	logger.info("Iniciou Funcao DumpTabela: {}".format(nome_da_tabela))

	if(not db.tabela_ja_criada(nome_da_tabela)):
		logger.info("Tabela {} não existe. Sugestão: Crie a tabela {}".format(nome_da_tabela, nome_da_tabela))
		return False
	elif(db.tabela_ja_povoada(nome_da_tabela)):
		logger.info("Tabela {} já foi povoada anteriormente.".format(nome_da_tabela))
		return False
	else:
		logger.info("Dump {} vai começar:".format(nome_da_tabela))
		offset = 0
		url = url_entidade.format('0')
		req = requests.get(url)
		json_ = req.json()

		limit = json_['count']

		logger.info("Quantidade de elementos: {}".format(limit))
		
		resultset = []

		flush_len = 10000

		while( offset < limit ):
			print(offset)

			url = url_entidade.format(offset)
			try:
				req = requests.get(url)
				json_ = req.json()
				
				for i in range(len(json_['_embedded'][elemento_json])):
					h = {key:value for (key, value) in json_['_embedded'][elemento_json][i].items() if (key in atributos_validos) }

					h.update({key:None for key in atributos_validos if key not in json_['_embedded'][elemento_json][i].keys()})
					
					resultset.append(h)


				if(offset == flush_len):
					db.bulk_insert(resultset, atributos_validos, nome_da_tabela)
					logger.info("Inseriu até {}".format(offset))
					resultset = []	

			except Exception as error:
				logger.error("Tabela {} - Timeout at offset {}".format(nome_da_tabela, offset))
				logger.error("Error: {}".format(error))
			

			offset = offset + 500



		if(len(resultset)):
			logger.info("Inseriu até {}", limit)
			db.bulk_insert(resultset, atributos_validos, nome_da_tabela)

		logger.info("Terminou Extração de {}", nome_da_tabela)
		db.insere_tabela_povoada(nome_da_tabela)
		logger.info("Gravou {} em 'tabelas_ja_povoadas'", nome_da_tabela)

		return True



def dump_uasgs():
	url_uasgs = "http://compras.dados.gov.br/licitacoes/v1/uasgs.json?offset={}"

	elemento_json = "uasgs"

	nome_da_tabela = "uasgs"

	atributos_uasgs = ['ativo', 'cep', 'ddd', 'endereco', 'fax', 'id', 'id_municipio', 
								'id_orgao', 'nome', 'nome_mnemonico', 'ramal', 'ramal2', 'sigla_uf', 

								'telefone', 'telefone2', 'unidade_cadastradora']


	return dump_tabela(url_uasgs, elemento_json, nome_da_tabela, atributos_uasgs)

