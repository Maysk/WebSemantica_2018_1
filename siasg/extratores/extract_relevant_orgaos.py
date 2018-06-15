import requests
import json 
import os
import database as db

url_uasg = "http://compras.dados.gov.br/licitacoes/v1/orgaos.json?offset={}"

#http://ck.govdata.gov.br/organization/mp
#https://www.governodigital.gov.br/noticias/novo-sicaf-agiliza-acesso-de-fornecedores-a-administracao-publica
#http://dados.gov.br/dataset/siorg

#http://www.comprasnet.gov.br/consultalicitacoes/ConsLicitacao_Filtro.asp?numprp=000032009&dt_publ_ini=&dt_publ_fim=&chkModalidade=1,2,3,20,5,99&chk_concor=31,32,41,42&chk_pregao=1,2,3,4&chk_rdc=1,2,3,4&optTpPesqMat=M&optTpPesqServ=S&chkTodos=-1&chk_concorTodos=-1&chk_pregaoTodos=-1&txtlstUf=&txtlstMunicipio=&txtlstUasg=153229&txtlstGrpMaterial=&txtlstClasMaterial=&txtlstMaterial=&txtlstGrpServico=&txtlstServico=&txtObjeto=153229
#https://www.comprasgovernamentais.gov.br/index.php/placar-licitacoes
#https://www.comprasgovernamentais.gov.br/index.php/consultass/81-gestor-de-compras/consultas/725-licitacoes-consultas
#http://comprasnet.gov.br/acesso.asp?url=/livre/Resultado/conrelit00.asp

lista_de_orgaos_ids = [element for (element,) in db.get_orgaos_relevantes()]

print (lista_de_orgaos_ids)

for orgao_id in lista_de_orgaos_ids:
	pass
