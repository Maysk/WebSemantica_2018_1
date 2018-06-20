import dump_exec_aux as aux


url_uasgs = "http://compras.dados.gov.br/licitacoes/v1/uasgs.json?offset={}"

elemento_json = "uasgs"

nome_da_tabela = "uasgs"

atributos_uasgs = ['ativo', 'cep', 'ddd', 'endereco', 'fax', 'id', 'id_municipio', 
							'id_orgao', 'nome', 'nome_mnemonico', 'ramal', 'ramal2', 'sigla_uf', 

							'telefone', 'telefone2', 'unidade_cadastradora']


aux.dump_tabela(url_uasgs, elemento_json, nome_da_tabela, atributos_uasgs)

