import requests
import json 
import os
import database as db

url_uasg = "http://compras.dados.gov.br/licitacoes/v1/orgaos.json?offset={}"

orgaos_id = db.get_orgaos_relevantes()
print (orgaos_id)
