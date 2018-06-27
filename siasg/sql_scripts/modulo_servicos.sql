# Tirados de http://compras.dados.gov.br/docs/lista-metodos-servicos.html

--secoes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/secoes.html

CREATE TABLE secoes_servicos(
	codigo INT,
	descricao TEXT
);

--divisoes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/divisoes.html

CREATE TABLE divisoes_servicos(
	codigo INT,
	codigo_secao INT,
	descricao TEXT
);

--grupos	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/grupos.html

CREATE TABLE grupos_servicos(
	codigo INT,
	codigo_divisao INT,
	descricao TEXT
);

--classes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/classes.html

CREATE TABLE classes_servicos(
	codigo INT,
	codigo_grupo INT,
	descricao TEXT
);

--subclasses	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/subclasses.html

CREATE TABLE subclasses_servicos(
	codigo INT,
	codigo_classe INT,
	descricao TEXT
);

--servicos	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/servicos.html

CREATE TABLE servicos(
	codigo INT,
	codigo_classe INT,
	codigo_divisao INT,
	codigo_grupo INT,
	codigo_secao INT,
	codigo_subclasse INT,
	cpc INT,
	descricao TEXT,
	unidade_medida TEXT
);
