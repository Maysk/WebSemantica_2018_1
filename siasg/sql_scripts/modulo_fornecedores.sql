-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-fornecedores.html

--ambitos_ocorrencia
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/ambitos_ocorrencia.html
CREATE TABLE ambitos_ocorrencia(
				id integer,
				descricao text
			);


--cnaes
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/cnaes.html
CREATE TABLE cnaes (
			id integer,
			descricao text,
			codigo_longo text
			)

--fornecedores:
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/fornecedores.html

CREATE TABLE fornecedores(
				ativo boolean, 
				cnpj text, 
				cpf text, 
				habilitado_licitar boolean,
				id integer,
				id_cnae integer,
				id_cnae2 integer,
				id_municipio integer,
				id_natureza_juridica integer,
				id_porte_empresa integer,
				id_ramo_negocio integer,
				id_unidade_cadastradora integer,
				nome text,
				recadastrado boolean,
				uf text
			);


--linhas_fornecimento
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/linhas_fornecimento.html
CREATE TABLE linhas_fornecimento(
				id integer,
				ativo boolean,
				codigo_material text,	
				codigo_servico text,
				tipo text
			);

CREATE TABLE linhas_fornecimento_fornecedor(
				id_fornecedor integer,
				id_linha_fornecimento integer
			);

--municipios
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/municipios.html
CREATE TABLE municipios(
				id integer,
				nome text,
				ativo boolean,
				codigo_ibge integer,
				nome_uf text,
				sigla_uf text
			);


--naturezas_juridicas
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/naturezas_juridicas.html
CREATE TABLE naturezas_juridicas(
				id integer,
				codigo text,
				descricao text,
				ativo boolean
			);

--ocorrencias_fornecedores
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/ocorrencias_fornecedores.html
CREATE TABLE ocorrencias_fornecedores(
				id integer,
				cnpj text,
				cpf text,
				id_orgao integer,
				id_tipo_ocorrencia integer,
				id_unidade_cadastradora integer,
				numero_processo text,
				tipo_pessoa text
			);


--portes_empresa
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/portes_empresa.html
CREATE TABLE portes_empresa(
			id integer,
			descricao text
		);

--prazos_ocorrencia
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/prazos_ocorrencia.html
CREATE TABLE prazos_ocorrencia(
			id integer,
			descricao text
		);

--ramos_negocio
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/ramos_negocio.html
CREATE TABLE ramos_negocio(
			id integer,
			descricao text,
			ativo boolean
		);


--tipos_ocorrencia
--	Link: http://compras.dados.gov.br/docs/fornecedores/v1/tipos_ocorrencia.html
CREATE TABLE tipos_ocorrencia(
			id integer,
			descricao text
		);

INSERT INTO tipos_ocorrencia (id, descricao) 
VALUES 	(6, 'Inativação a Pedido do Fornecedor'), 
	(8, 'Legado'), 
	(1, 'Advertência - Lei nº 8666/93, art. 87, inc. I'),
	(2, 'Multa - Lei nº 8666/93, art. 87, inc. II'),
	(3, 'Suspensão Temporária - Lei nº 8666/93, art. 87, inc. III'),
	(10, 'Dinâmica'),
	(4, 'Declaração de Inidoneidade - Lei nº 8666/93, art. 87, inc. IV'),
	(5, 'Impedimento de Licitar e Contratar - Lei nº 10.520/02, art. 7º'),
	(9, 'Reativação a Pedido do Fornecedor'),
	(7, 'Outros Tipos de Ocorrência');