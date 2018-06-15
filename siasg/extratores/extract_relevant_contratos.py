import requests
import json 
import os
import database as db

url_contratos = "http://compras.dados.gov.br/contratos/v1/contratos.json?offset={}"

lista_de_uasgs = [element for (element,) in db.get_uasgs_relevantes()]

atributos_validos = ["cnpj_contratada", "codigo_contrato", "cpfContratada", 
						"data_assinatura", "data_inicio_vigencia", "data_termino_vigencia", 
						"fundamento_legal", "identificador", "licitacao_associada", 
						"modalidade_licitacao", "numero", "numero_aditivo", 
						"numero_aviso_licitacao ", "numero_processo", "objeto", 
						"origem_licitacao", "uasg", "valor_inicial"]

offset = 0

url = url_contratos.format('0')

req = requests.get(url)

contrato_json = req.json()

limit = contrato_json['count']

resultset = []

while(offset<limit):
	print(offset)
	url = url_contratos.format(offset)
	try:
		req = requests.get(url, timeout = 3)
		contrato_json = req.json()
		for i in range(len(contrato_json['_embedded']['contratos'])):
			#if (contrato_json['_embedded']['uasg'][i]['uasg'] in id_):	
			h = {key:value for (key, value) in contrato_json['_embedded']['contratos'][i].items() if (key in atributos_validos) }
			h.update({key:None for key in atributos_validos if key not in contrato_json['_embedded']['contratos'][i].keys()})
			resultset.append(h)
	except Exception as error:
		print("Timeout at offset", offset)
		print (error)

		
	offset = offset + 500




print(len(resultset))

print("Deu Certo")


db.bulk_insert_contratos(resultset, atributos_validos)