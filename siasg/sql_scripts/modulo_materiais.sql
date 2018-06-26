-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-materiais.html

--classes	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/classes.html

CREATE TABLE classes (
	codigo       integer,
	codigo_grupo integer,
	descricao    text
);

--grupos	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/grupos.html

CREATE TABLE grupos (
	codigo    integer,
	descricao text
);

--pdms	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/pdms.html

CREATE TABLE pdms (
	codigo        text,
	codigo_classe integer,
	descricao     text
);


--materiais	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/materiais.html

CREATE TABLE materiais (
	codigo      integer,
	descricao   text,
	id_classe   integer,
	id_grupo    integer,
	id_pdm      text,
	status      boolean,
	sustentavel boolean
);

