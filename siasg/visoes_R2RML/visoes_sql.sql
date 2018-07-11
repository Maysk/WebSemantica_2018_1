CREATE OR REPLACE VIEW municipios_do_ceara AS 
 SELECT municipios.id,
    municipios.nome,
    municipios.ativo,
    municipios.codigo_ibge,
    municipios.nome_uf,
    municipios.sigla_uf
   FROM municipios
  WHERE municipios.sigla_uf ~~ 'CE'::text;


CREATE OR REPLACE VIEW uasgs_do_ceara AS 
 SELECT uasgs.ativo,
    uasgs.cep,
    uasgs.ddd,
    uasgs.endereco,
    uasgs.fax,
    uasgs.id,
    uasgs.id_municipio,
    uasgs.id_orgao,
    uasgs.nome,
    uasgs.nome_mnemonico,
    uasgs.ramal,
    uasgs.ramal2,
    uasgs.sigla_uf,
    uasgs.telefone,
    uasgs.telefone2,
    uasgs.unidade_cadastradora
   FROM uasgs
  WHERE (uasgs.id_municipio IN ( SELECT municipios_do_ceara.id
           FROM municipios_do_ceara));


CREATE OR REPLACE VIEW licitacoes_do_ceara AS 
 SELECT licitacoes.data_abertura_proposta,
    licitacoes.data_entrega_edital,
    licitacoes.data_entrega_proposta,
    licitacoes.data_publicacao,
    licitacoes.endereco_entrega_edital,
    licitacoes.funcao_responsavel,
    licitacoes.identificador,
    licitacoes.informacoes_gerais,
    licitacoes.modalidade,
    licitacoes.nome_responsavel,
    licitacoes.numero_aviso,
    licitacoes.numero_itens,
    licitacoes.numero_processo,
    licitacoes.objeto,
    licitacoes.situacao_aviso,
    licitacoes.tipo_pregao,
    licitacoes.tipo_recurso,
    licitacoes.uasg
   FROM licitacoes
  WHERE (licitacoes.uasg IN ( SELECT uasgs_do_ceara.id
           FROM uasgs_do_ceara));


CREATE OR REPLACE VIEW contratos_do_ceara AS 
 SELECT contratos.cnpj_contratada,
    contratos.codigo_contrato,
    contratos.cpfcontratada,
    contratos.data_assinatura,
    contratos.data_inicio_vigencia,
    contratos.data_termino_vigencia,
    contratos.fundamento_legal,
    contratos.identificador,
    contratos.licitacao_associada,
    contratos.modalidade_licitacao,
    contratos.numero,
    contratos.numero_aditivo,
    contratos.numero_aviso_licitacao,
    contratos.numero_processo,
    contratos.objeto,
    contratos.origem_licitacao,
    contratos.uasg,
    contratos.valor_inicial
   FROM contratos
  WHERE (contratos.uasg IN ( SELECT uasgs_do_ceara.id
           FROM uasgs_do_ceara));