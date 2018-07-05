create table item_licitacao(
	numero_licitacao text,
	cnpj_vencedor text,
	nome_vencedor text, 
	numero_item text,
	descricao text,
	quantidade_item text,
	valor_item text
);


create table licitacao(
	numero_licitacao text,
	numero_processo text,
	objeto text,
	modalidade_compra text,
	situacao_licitacao text,
	codigo_orgao_superior text,
	nome_orgao_superior text,
	codigo_orgao text,
	nome_orgao text,
	codigo_ug text,
	nome_ug text,
	municipio text, 
	data_publicacao_dou text,
	data_abertura text,
	valor_licitacao text
);

create table participante_licitacao(
	numero_licitacao text, 
	codigo_item_compra text,
	descricao_item_compra text,
	cnpj_participante text, 
	nome_participante text,
	flag_vencedor text
);