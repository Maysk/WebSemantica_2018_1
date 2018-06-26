-- Tirados de http://compras.dados.gov.br/docs/lista-metodos-compraSemLicitacao.html

--compras_sem_licitacao:
--	Link: http://compras.dados.gov.br/docs/compraSemLicitacao/v1/compras_slicitacao.html

-- Table: compras_sem_licitacao:

CREATE TABLE compras_sem_licitacao
(
    co_modalidade_licitacao integer,
    co_orgao text,
    co_uasg integer,
    
    ds_fundamento_legal text,
    ds_justificativa text,
    ds_lei text,
    ds_objeto_licitacao text,
    
    dtPublicacao text,
    dtRatificacao text,
    dtDeclaracaoDispensa text,
    
    no_cargo_resp_decl_disp text,
    no_cargo_resp_ratificacao text,
    no_responsavel_decl_disp text,
    no_responsavel_ratificacao text,
    
    nu_inciso text,
    nu_processo text,
    nu_aviso_licitacao text,
    
    qt_total_item text,
    vr_estimado real
)

--itens_compras_sem_licitacao	
--	Link: http://compras.dados.gov.br/docs/compraSemLicitacao/v1/itens_compras_slicitacao.html

-- Table: itens_compras_sem_licitacao

CREATE TABLE itens_compras_sem_licitacao
(
    co_modalidade_licitacao integer,
    co_orgao text,
    co_uasg integer,

    ds_fundamento_legal text,
    ds_justificativa text,
    ds_lei text,
    ds_objeto_licitacao text,


    dtDeclaracaoDispensa text,
    dtRatificacao text,
    dtPublicacao text,

    no_responsavel_decl_disp text,
    no_cargo_resp_decl_disp text,
    no_responsavel_ratificacao text,
    no_cargo_resp_ratificacao text,

    nu_inciso text,
    nu_processo text,
    nu_aviso_licitacao text,

    qt_total_item text,
    vr_estimado real

)
