-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-materiais.html

--classes	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/classes.html

--grupos	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/grupos.html

--pdms	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/pdms.html

--materiais	
--	Link: http://compras.dados.gov.br/docs/materiais/v1/materiais.html

CREATE TABLE classes (
codigo       integer,
codigo_grupo integer,
descricao    text,
);

CREATE TABLE grupos (
codigo    integer,
descricao text,
);

CREATE TABLE pdms (
codigo        integer,
codigo_classe integer,
descricao     text
);

CREATE TABLE materiais (
codigo      integer,
descricao   text,
id_classe   integer,
id_grupo    integer,
id_pdm      integer,
status      boolean,
sustentavel boolean,
);
