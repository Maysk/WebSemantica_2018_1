-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-licitacoes.html

--irps	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/irps.html
CREATE TABLE irps(
				cpf_responsavel text, 
				data_provavel_licitacao text,
				justificativa_modalidade text,
				modalidade_licitacao integer,
				municipio integer,
				nome_responsavel text,
				numero_irp integer,
				objeto text,
				orgao integer,
				prazo_validade text,
				sigla_uf text,
				situacao text,
				tipo_licitacao text,
				uasg integer
			);

--itens_irp	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_irp.html

--participantes_item_irp	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/participantes_item_irp.html

--licitacoes	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/licitacoes.html

CREATE TABLE licitacoes(
				data_abertura_proposta text,
				data_entrega_edital text,
				data_entrega_proposta text,
				data_publicacao text,
				endereco_entrega_edital text,
				funcao_responsavel text,
				identificador text,
				informacoes_gerais text,
				modalidade integer, 
				nome_responsavel text,
				numero_aviso integer, 
				numero_itens integer,
				numero_processo text,
				objeto text,
				situacao_aviso text,
				tipo_pregao text,
				tipo_recurso text,
				uasg integer
			);

--itens_licitacao	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_licitacao.html

--modalidades_licitacao	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/modalidades_licitacao.html

CREATE TABLE modalidades_licitacao(
				codigo integer,
				descricao text
			);
		
--orgaos	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/orgaos.html
CREATE TABLE orgaos(
				ativo boolean,
				codigo integer,
				codigo_siorg text,
				codigo_tipo_adm integer,
				codigo_tipo_esfera text,
				codigo_tipo_poder integer,
				nome text
			);

--precos_praticados	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/precos_praticados.html

CREATE TABLE precos_praticados(
				id_licitacao text,
				modalidade integer,
				numero_aviso integer,
				numero_itens integer,
				objeto text,
				situacao text,
				uasg integer,
				valor_total real
			);

--itens_preco_praticado	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_preco_praticado.html

--registros_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/registros_preco.html
CREATE TABLE registros_preco(
				data_assinatura text,
				data_fim_validade text,
				data_inicio_validade text,
				id_licitacao text,
				modalidade integer,
				numero_aviso integer,
				numero_itens integer,
				situacao text,
				uasg integer,
				valor_renegociado real, 
				valor_total real 
);

--itens_registro_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_registro_preco.html

--fornecedores_item_registro_preco	 
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/fornecedores_item_registro_preco.html

--renegociacoes_fornecedor_item_registro_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/renegociacoes_fornecedor_item_registro_preco.html

--uasgs	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/uasgs.html
CREATE TABLE uasgs(
				ativo boolean,
				cep text,
				ddd text ,
				endereco text,
				fax text,
				id integer,
				id_municipio integer,
				id_orgao integer,
				nome text,
				nome_mnemonico text,
				ramal text,
				ramal2 text,
				sigla_uf text,
				telefone text,
				telefone2 text,
				unidade_cadastradora boolean
			);

--rdcs	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/rdcs.html

CREATE TABLE rdcs(
				data_abertura_proposta text,
				data_entrega_edital text,
				data_entrega_proposta text,
				data_publicacao text,
				endereco_entrega_edital text,
				forma_de_realizacao_licitacao text,
				funcao_responsavel text,
				identificador text,
				informacoes_gerais text, 
				modalidade integer,
				nome_responsavel text,
				numero_aviso integer,
				numero_itens integer,
				numero_processo text,
				objeto text,
				situacao_aviso text,
				tipo_recurso text,
				uasg integer
			);
