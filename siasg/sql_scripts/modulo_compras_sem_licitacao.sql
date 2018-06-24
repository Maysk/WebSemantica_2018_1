-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-compraSemLicitacao.html

--compras_sem_licitacao:
--	Link: http://compras.dados.gov.br/docs/compraSemLicitacao/v1/compras_slicitacao.html

-- Table: compras_sem_licitacao:

CREATE TABLE compras_sem_licitacao
(
  id integer,
  co_orgao text,
  co_uasg integer,
  co_modalidade_licitacao integer,
  nu_inciso text,
  nu_processo text,
  vr_estimado real,
  ds_fundamento_legal text,
  ds_justificativa text,
  "dtDeclaracaoDispensa" time with time zone,
  no_responsavel_decl_disp text,
  no_cargo_resp_decl_disp text,
  "dtRatificacao" time with time zone,
  no_responsavel_ratificacao text,
  no_cargo_resp_ratificacao text,
  "dtPublicacao" time with time zone,
  _links text,
  itens integer
)

--itens_compras_sem_licitacao	
--	Link: http://compras.dados.gov.br/docs/compraSemLicitacao/v1/itens_compras_slicitacao.html

-- Table: itens_compras_sem_licitacao

CREATE TABLE itens_compras_sem_licitacao
(
  id integer,
  co_modalidade_licitacao integer,
  nu_inciso text,
  nu_processo text,
  vr_estimado real,
  ds_fundamento_legal text,
  ds_justificativa text,
  "dtDeclaracaoDispensa" time with time zone,
  no_responsavel_decl_disp text,
  no_cargo_resp_decl_disp text,
  _links integer,
  itens integer,
  co_orgao text,
  co_uasg integer,
  "dtRatificacao" time with time zone,
  no_responsavel_ratificacao text,
  no_cargo_resp_ratificacao text,
  "dtPublicacao" time with time zone
)

--tabelas relacionadas
-- Table: _links
CREATE TABLE _links
(
  id integer,
  self text,
  title text
)

-- Table: itens

CREATE TABLE itens
(
  id integer,
  href text,
  title text
)

-- Table: modalidade_licitacao

CREATE TABLE modalidade_licitacao
(
  id integer,
  href text,
  title text
)

-- Table: orgao

CREATE TABLE orgao
(
  id text,
  title text,
  href text
)

-- Table: uasg

CREATE TABLE uasg
(
  id integer,
  href text,
  title text
)