# Tirados de http://compras.dados.gov.br/docs/lista-metodos-servicos.html

--secoes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/secoes.html

CREATE TABLE Secoes(
	codigo INT,
	descricao TEXT
);

--divisoes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/divisoes.html

CREATE TABLE Divisoes(
	codigo INT,
	codigo_secao INT,
	descricao TEXT
);

--grupos	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/grupos.html

CREATE TABLE Grupos(
	codigo INT,
	codigo_divisao INT,
	descricao TEXT
);

--classes	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/classes.html

CREATE TABLE Classes(
	codigo INT,
	codigo_grupo INT,
	descricao TEXT
);

--subclasses	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/subclasses.html

CREATE TABLE Subclasses(
	codigo INT,
	codigo_classe INT,
	descricao TEXT
);

--servicos	
--	Link: http://compras.dados.gov.br/docs/servicos/v1/servicos.html

CREATE TABLE Servicos(
	codigo INT,
	codigo_classe INT,
	codigo_divisao INT,
	codigo_grupo INT,
	codigo_secao INT,
	codigo_subclasse INT,
	descricao TEXT,
	unidade_medida TEXT
);
