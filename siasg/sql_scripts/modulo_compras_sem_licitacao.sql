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

#Temporaria
CREATE TABLE compras_sem_licitacao_do_ceara_item
(
    co_conjunto_materiais integer, 
    co_servico integer,
    ds_detalhada text,
    ds_tipo_fornecedor_vencedor text,
    fornecedor text,
    no_conjunto_materiais text,
    no_marca_material text, 
    no_servico text,
    no_unidade_medida text,
    nu_cnpj_vencedor text,
    nu_cpf_vencedor text, 
    qt_material_alt text
    vr_estimado real
);

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
