CREATE TABLE item_compra(
		numero_contrato text,
		codigo_item_compra text,
		descricao_item_compra text,
		quantidade_item_compra text,
		valor_item text
	);

CREATE TABLE contratos(
		numero_contrato text,
		objeto text,
		fundamento_legal text,
		modalidade_compra text,
		situacao_contrato text,
		codigo_orgao_superior text,
		nome_orgao_superior text,
		codigo_orgao text,
		nome_orgao text,
		codigo_ug text,
		nome_ug text,
		data_assinatura_contrato text,
		data_publicacao_dou text,
		data_inicio_vigencia text,
		data_fim_vigencia text,
		cnpj_contratado text,
		nome_contratado text,
		valor_inicio_compra text,
		valor_final_compra text
	);

CREATE TABLE termo_aditivo(
		numero_contrato text,
		numero_termo_aditivo text,
		data_publicacao text,
		objeto text
	);