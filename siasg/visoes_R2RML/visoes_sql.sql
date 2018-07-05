-- Todas as UASGS do Ceara 

--SELECT *
--FROM uasgs
--WHERE sigla_uf='CE'

-- Todos os Orgaos relacionados as UASGS do Ceara

--SELECT *
--FROM orgaos O, uasgs U
--WHERE O.codigo = U.id_orgao
--AND U.sigla_uf = 'CE'

-- Todos os contratos ligados as UASGS do Ceara

--SELECT *
--FROM contratos C, uasgs U
--WHERE C.uasg = U.id
--AND U.sigla_uf  = 'CE'

-- Todas as licitações ligadas as uasgs do Ceara

--SELECT *
--FROM licitacoes L, uasgs U
--WHERE L.uasg = U.id
--AND U.sigla_uf  = 'CE'

