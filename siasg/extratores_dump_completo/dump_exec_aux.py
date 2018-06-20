import requests
import json 
import os
import database as db
import logging

testing = False

logger = logging.getLogger("MainExtractor.ExecAux")

def dump_tabela(url_entidade, elemento_json, nome_da_tabela, atributos_validos):
	logger.info("Iniciou Funcao DumpTabela: {}".format(nome_da_tabela))

	if(not db.tabela_ja_criada(nome_da_tabela)):
		logger.info("Tabela {} não existe. Sugestão: Crie a tabela {}".format(nome_da_tabela, nome_da_tabela))
		return False
	elif(db.tabela_ja_povoada(nome_da_tabela)):
		logger.info("Tabela {} já foi povoada anteriormente.".format(nome_da_tabela))
		return True
	else:
		logger.info("Dump {} vai começar:".format(nome_da_tabela))
		print("\n\nDump {} vai começar:".format(nome_da_tabela))
		offset = 0
		url = url_entidade.format('0')
		req = requests.get(url)
		json_ = req.json()

		if testing:
			limit = 500
		else:
			limit = json_['count']

		logger.info("Quantidade de elementos: {}".format(limit))
		
		resultset = []

		flush_len = 10000
		flush_counter = 0

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

					flush_counter = flush_counter + 1


				if(flush_counter == flush_len):
					db.bulk_insert(resultset, atributos_validos, nome_da_tabela)
					logger.info("Inseriu até {}".format(offset))
					resultset = []	
					flush_counter = 0

			except Exception as error:
				logger.error("Tabela {} - Timeout at offset {}".format(nome_da_tabela, offset))
				logger.error("Error: {}".format(error))
			

			offset = offset + 500



		if(len(resultset) > 0):
			logger.info("Inseriu até {}".format(limit))
			db.bulk_insert(resultset, atributos_validos, nome_da_tabela)

		logger.info("Terminou Extração de {}".format(nome_da_tabela))
		db.insere_tabela_povoada(nome_da_tabela)
		logger.info("Gravou {} em 'tabelas_ja_povoadas'".format(nome_da_tabela))

		return True



def dump_uasgs():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/uasgs.json?offset={}"

	elemento_json = "uasgs"

	nome_da_tabela = "uasgs"

	atributos_considerados = ['ativo', 'cep', 'ddd', 'endereco', 'fax', 'id', 'id_municipio', 
								'id_orgao', 'nome', 'nome_mnemonico', 'ramal', 'ramal2', 'sigla_uf', 

								'telefone', 'telefone2', 'unidade_cadastradora']


	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_orgaos():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/orgaos.json?offset={}"

	elemento_json = "Orgaos"

	nome_da_tabela = "orgaos"

	atributos_considerados = ['ativo', 'codigo', 'codigo_siorg', 'codigo_tipo_adm', 'codigo_tipo_esfera', 'codigo_tipo_poder', 'nome']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_licitacoes():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/licitacoes.json?offset={}"

	elemento_json = "licitacoes"

	nome_da_tabela = "licitacoes"

	atributos_considerados = ['data_abertura_proposta', 'data_entrega_edital', 'data_entrega_proposta', 'data_publicacao', 'endereco_entrega_edital', 
							'funcao_responsavel', 'identificador', 'informacoes_gerais', 'modalidade', 'nome_responsavel', 
							'numero_aviso', 'numero_itens', 'numero_processo', 'objeto', 'situacao_aviso', 'tipo_pregao', 'tipo_recurso', 'uasg']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_modalidades_licitacoes():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/modalidades_licitacao.json?offset={}"

	elemento_json = "ModalidadesLicitacao"

	nome_da_tabela = "modalidades_licitacao"

	atributos_considerados = ['codigo', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)
