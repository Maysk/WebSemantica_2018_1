import requests
import json 
import os
import database as db
id_ = [13897]

url_uasg = "http://compras.dados.gov.br/licitacoes/v1/uasgs.json?offset={}"

offset = 0
url = url_uasg.format('0')

req = requests.get(url)

uasg_json = req.json()

limit = 500#uasg_json['count']

resultset = []
while(offset<limit):
	print(offset)
	url = url_uasg.format(offset)
	req = requests.get(url)
	uasg_json = req.json()
	for i in range(len(uasg_json['_embedded']['uasgs'])):
		#if (uasg_json['_embedded']['uasgs'][i]['id'] in id_):
		#	print("Aqui")
		resultset.append(uasg_json['_embedded']['uasgs'][i])
		
	offset = offset + 500

print(len(resultset))

print("Deu Certo")

for r in resultset:
	print(r)	
	print("Inserindo no banco...")
	db.insert_uasg(r['ativo'], r['cep'], r['id'], r['id_municipio'], r['id_orgao'], r['nome'], r['unidade_cadastradora'])

		
		
		
