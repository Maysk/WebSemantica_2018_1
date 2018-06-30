CREATE TABLE receita_cnpj_info_empresa (
	cnpj             varchar(14),
	nome_empresarial varchar(150),
    
);

CREATE TABLE receita_cnpj_info_socio(
	cnpj	           varchar(14),
	indicador_cpf_cnpj varchar(1),
	cpf_cnpj           varchar(14),
	qualificacao_socio varchar(2),
	nome_socio         varchar(150)
	
);
