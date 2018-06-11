-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-licitacoes.html

--irps	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/irps.html

--itens_irp	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_irp.html

--participantes_item_irp	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/participantes_item_irp.html

--licitacoes	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/licitacoes.html
CREATE TABLE UASGS(
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
				total_fornecedores_cadastrados integer,
				total_fornecedores_recadastrados integer,
				unidade_cadastradora boolean
			);


--itens_licitacao	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_licitacao.html

--modalidades_licitacao	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/modalidades_licitacao.html

--orgaos	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/orgaos.html

--precos_praticados	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/precos_praticados.html

--itens_preco_praticado	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_preco_praticado.html

--registros_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/registros_preco.html

--itens_registro_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/itens_registro_preco.html

--fornecedores_item_registro_preco	 
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/fornecedores_item_registro_preco.html

--renegociacoes_fornecedor_item_registro_preco	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/renegociacoes_fornecedor_item_registro_preco.html

--uasgs	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/uasgs.html

--rdcs	
--	Link: http://compras.dados.gov.br/docs/licitacoes/v1/rdcs.html