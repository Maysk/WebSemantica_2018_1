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
			limit = 1000
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



################################################################
###################### MODULO LICITACOES #######################
################################################################

def dump_irps():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/irps.json?offset={}"

	elemento_json = "irps"

	nome_da_tabela = "irps"

	atributos_considerados = ['cpf_responsavel', 'data_provavel_licitacao',	'justificativa_modalidade', 'modalidade_licitacao',		
								'municipio', 'nome_responsavel', 'numero_irp', 'objeto', 'orgao', 'prazo_validade',	'sigla_uf',
								'situacao', 'tipo_licitacao', 'uasg']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_precos_praticados():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/precos_praticados.json?offset={}"

	elemento_json = "precosPraticados"

	nome_da_tabela = "precos_praticados"

	atributos_considerados = ['id_licitacao', 'modalidade',	'numero_aviso', 'numero_itens',	'objeto',
								'situacao', 'uasg', 'valor_total'	]

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_registros_preco():
	url_ = "http://compras.dados.gov.br/licitacoes/v1/registros_preco.json?offset={}"

	elemento_json = "registrosPreco"

	nome_da_tabela = "registros_preco"

	atributos_considerados = [ 'data_assinatura', 'data_fim_validade', 'data_inicio_validade', 'id_licitacao', 
								'modalidade', 'numero_aviso', 'numero_itens', 'situacao', 'uasg', 
								'valor_renegociado', 'valor_total' ]

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


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




################################################################
###################### MODULO CONTRATOS ########################
################################################################

def dump_contratos():
	url_ = "http://compras.dados.gov.br/contratos/v1/contratos.json?offset={}"

	elemento_json = "contratos"

	nome_da_tabela = "contratos"

	atributos_considerados = ['cnpj_contratada', 'codigo_contrato', 'cpfContratada', 'data_assinatura', 'data_inicio_vigencia', 'data_termino_vigencia', 'fundamento_legal', 'identificador', 'licitacao_associada', 'modalidade_licitacao', 'numero', 'numero_aditivo', 'numero_aviso_licitacao', 'numero_processo', 'objeto', 'origem_licitacao', 'uasg', 'valor_inicial']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


################################################################
###################### MODULO FORNECEDORES #####################
################################################################

def dump_cnaes():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/cnaes.json?offset={}"

	elemento_json = "cnaes"

	nome_da_tabela = "cnaes"

	atributos_considerados = ['id', 'descricao', 'codigo_longo']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_municipios():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/municipios.json?offset={}"

	elemento_json = "municipios"

	nome_da_tabela = "municipios"

	atributos_considerados = ['ativo', 'codigo_ibge', 'id', 'nome', 'nome_uf', 'sigla_uf']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_ramos_negocio():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/ramos_negocio.json?offset={}"

	elemento_json = "ramosNegocio"

	nome_da_tabela = "ramos_negocio"

	atributos_considerados = ['ativo', 'descricao', 'id']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_portes_empresa():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/portes_empresa.json?offset={}"

	elemento_json = "portesEmpresa"

	nome_da_tabela = "portes_empresa"

	atributos_considerados = ['descricao', 'id']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_linhas_fornecimento():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/linhas_fornecimento.json?offset={}"

	elemento_json = "linhasFornecimento"

	nome_da_tabela = "linhas_fornecimento"

	atributos_considerados = ['ativo', 'id', 'tipo', 'codigo_material', 'codigo_servico']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_fornecedores():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/fornecedores.json?offset={}"

	elemento_json = "fornecedores"

	nome_da_tabela = "fornecedores"

	atributos_considerados = ['ativo', 'cnpj', 'cpf', 'habilitado_licitar', 'id', 'id_cnae', 
							'id_cnae2','id_municipio', 'id_natureza_juridica', 'id_porte_empresa',
							'id_ramo_negocio', 'id_unidade_cadastradora', 'nome',
							'recadastrado', 'uf']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_ocorrencias_fornecedores():
	url_ = "http://compras.dados.gov.br/fornecedores/v1/ocorrencias_fornecedores.json?offset={}"

	elemento_json = "ocorrenciasFornecedores"

	nome_da_tabela = "ocorrencias_fornecedores"

	atributos_considerados = ['id', 'cnpj', 'cpf', 'id_orgao', 'id_tipo_ocorrencia', 'id_unidade_cadastradora', 'numero_processo', 'tipo_pessoa']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)




################################################################
################# MODULO COMPRAS SEM LICITACAO #################
################################################################


def dump_compras_sem_licitacao():
	url_ = "http://compras.dados.gov.br/compraSemLicitacao/v1/compras_slicitacao.json?offset={}"

	elemento_json = "compras"

	nome_da_tabela = "compras_sem_licitacao"

	atributos_considerados = ['co_modalidade_licitacao', 'co_orgao', 'co_uasg', 'ds_fundamento_legal', 'ds_justificativa', 
							'ds_lei', 'ds_objeto_licitacao', 'dtPublicacao', 'dtRatificacao', 'dtDeclaracaoDispensa', 
							'no_cargo_resp_decl_disp', 'no_cargo_resp_ratificacao', 'no_responsavel_decl_disp', 'no_responsavel_ratificacao', 
							'nu_inciso', 'nu_processo', 'nu_aviso_licitacao', 'qt_total_item', 'vr_estimado']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_itens_compras_sem_licitacao():
	url_ = "http://compras.dados.gov.br/compraSemLicitacao/v1/itens_compras_slicitacao.json?offset={}"

	elemento_json = "compras"

	nome_da_tabela = "itens_compras_sem_licitacao"

	atributos_considerados = ['co_modalidade_licitacao', 'co_orgao', 'co_uasg', 'ds_fundamento_legal', 'ds_justificativa', 
							'ds_lei', 'ds_objeto_licitacao', 'dtPublicacao', 'dtRatificacao', 'dtDeclaracaoDispensa', 
							'no_cargo_resp_decl_disp', 'no_cargo_resp_ratificacao', 'no_responsavel_decl_disp', 'no_responsavel_ratificacao', 
							'nu_inciso', 'nu_processo', 'nu_aviso_licitacao', 'qt_total_item', 'vr_estimado']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


################################################################
####################### MODULO MATERIAIS #######################
################################################################

def dump_classes():
	url_ = "http://compras.dados.gov.br/materiais/v1/classes.json?offset={}"

	elemento_json = "classes"

	nome_da_tabela = "classes"

	atributos_considerados = ['codigo', 'codigo_grupo', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_grupos():
	url_ = "http://compras.dados.gov.br/materiais/v1/grupos.json?offset={}"

	elemento_json = "grupos"

	nome_da_tabela = "grupos"

	atributos_considerados = ['codigo', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_pdms():
	url_ = "http://compras.dados.gov.br/materiais/v1/pdms.json?offset={}"

	elemento_json = "pdms"

	nome_da_tabela = "pdms"

	atributos_considerados = ['codigo', 'codigo_classe', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_materiais():
	url_ = "http://compras.dados.gov.br/materiais/v1/materiais.json?offset={}"

	elemento_json = "materiais"

	nome_da_tabela = "materiais"

	atributos_considerados = 	['codigo', 'descricao', 'id_classe', 'id_grupo', 'id_pdm', 'status', 'sustentavel']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


################################################################
######################## MODULO SERVICOS #######################
################################################################

def dump_secoes_servicos():
	url_ = "http://compras.dados.gov.br/servicos/v1/secoes.json?offset={}"

	elemento_json = "secoes"

	nome_da_tabela = "secoes_servicos"

	atributos_considerados = ['codigo', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_divisoes_servicos():
	url_ = "http://compras.dados.gov.br/servicos/v1/divisoes.json?offset={}"

	elemento_json = "divisoes"

	nome_da_tabela = "divisoes_servicos"

	atributos_considerados = ['codigo', 'codigo_secao', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_grupos_servicos():
	url_ = "http://compras.dados.gov.br/servicos/v1/grupos.json?offset={}"

	elemento_json = "grupos"

	nome_da_tabela = "grupos_servicos"

	atributos_considerados = ['codigo', 'codigo_divisao', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_classes_servicos():
	url_ = "http://compras.dados.gov.br/materiais/v1/classes.json?offset={}"

	elemento_json = "classes"

	nome_da_tabela = "classes_servicos"

	atributos_considerados = ['codigo', 'codigo_grupo', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)

def dump_subclasses_servicos():
	url_ = "http://compras.dados.gov.br/servicos/v1/subclasses.json?offset={}"

	elemento_json = "subclasses"

	nome_da_tabela = "subclasses_servicos"

	atributos_considerados = ['codigo', 'codigo_classe', 'descricao']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)


def dump_servicos():
	url_ = "http://compras.dados.gov.br/servicos/v1/servicos.json?offset={}"

	elemento_json = "servicos"

	nome_da_tabela = "servicos"

	atributos_considerados = ['codigo', 'codigo_classe', 'codigo_divisao', 'codigo_grupo', 
							'codigo_secao', 'codigo_subclasse', 'cpc', 'descricao', 'unidade_medida']

	return dump_tabela(url_, elemento_json, nome_da_tabela, atributos_considerados)
