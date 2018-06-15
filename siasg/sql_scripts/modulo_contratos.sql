--Tirados de http://compras.dados.gov.br/docs/lista-metodos-contratos.html

--contratos	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/contratos.html
CREATE TABLE contratos(
				cnpj_contratada text,
				codigo_contrato text,
				cpfContratada text,
				data_assinatura date,
				data_inicio_vigencia date,
				data_termino_vigencia date,
				fundamento_legal text,
				identificador text,
				licitacao_associada text,
				modalidade_licitacao integer,
				numero integer,
				numero_aditivo integer,
				numero_aviso_licitacao integer, 
				numero_processo text,
				objeto text,
				origem_licitacao text,
				uasg integer,
				valor_inicial real
			);

--aditivos_contratos	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/aditivos_contratos.html

--apostilamentos_contratos	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/apostilamentos_contratos.html

--tipos_contrato	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/tipos_contrato.html

--cronogramas	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/cronogramas.html

--eventos_contrato	
--	Link: http://compras.dados.gov.br/docs/contratos/v1/eventos_contrato.html