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


atributos_validos = ['ativo', 'cep', 'ddd', 'endereco', 'fax', 'id', 'id_municipio', 
						'id_orgao', 'nome', 'nome_mnemonico', 'ramal', 'ramal2', 'sigla_uf', 
						'telefone', 'telefone2', 'unidade_cadastradora']

resultset = []

#https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression

while(offset<limit):
	print(offset)
	url = url_uasg.format(offset)
	req = requests.get(url)
	uasg_json = req.json()
	
	for i in range(len(uasg_json['_embedded']['uasgs'])):
		if ('id_municipio' in uasg_json['_embedded']['uasgs'][i] and uasg_json['_embedded']['uasgs'][i]['id_municipio'] in id_):	
			h = {key:value for (key, value) in uasg_json['_embedded']['uasgs'][i].items() if (key in atributos_validos) }
			h.update({key:None for key in atributos_validos if key not in uasg_json['_embedded']['uasgs'][i].keys()})
			resultset.append(h)


		
	offset = offset + 500




print(len(resultset))

print("Deu Certo")


db.bulk_insert_uasg(resultset, atributos_validos)
		
		
#https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
