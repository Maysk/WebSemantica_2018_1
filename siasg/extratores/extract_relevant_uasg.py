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

limit = uasg_json['count']

resultset = []
while(offset<limit):
	print(offset)
	url = url_uasg.format(offset)
	req = requests.get(url)
	uasg_json = req.json()
	for i in range(len(uasg_json['_embedded']['uasgs'])):
		if ('id_municipio' in uasg_json['_embedded']['uasgs'][i] 
				and uasg_json['_embedded']['uasgs'][i]['id_municipio'] in id_):
			print("Aqui")
			resultset.append(uasg_json['_embedded']['uasgs'][i])
		
	offset = offset + 500

print(len(resultset))

print("Deu Certo")

#Helped 
#https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
i = 0
for uasg in resultset:
	if i % 500 == 0:  
		print("Inseriu: ", i)
	atributos_validos = ['ativo', 'cep', 'ddd', 'endereco', 'fax', 'id', 'id_municipio', 
						'id_orgao', 'nome', 'nome_mnemonico', 'ramal', 'ramal2', 'sigla_uf', 
						'telefone', 'telefone2', 'unidade_cadastradora']

	h = {key:value for (key,value) in uasg.items() if key in atributos_validos}
	db.insert_uasg(**h)
	i = i + 1

		
		
		
