import requests
import json 
import os
import database as db

def dump_tabela(url_entidade, elemento_json, nome_da_tabela, atributos_validos):

	offset = 0

	url = url_entidade.format('0')

	req = requests.get(url)

	json_ = req.json()

	limit = 1000#json_['count']

	print("Limit: ", limit)

	resultset = []

	flush_len = 10000

	while( offset < limit ):
		print(offset)

		url = url_entidade.format(offset)
		try:
			req = requests.get(url)
			json_ = req.json()
			
			for i in range(len(json_['_embedded'][elemento_json])):
				h = {key:value for (key, value) in json_['_embedded'][elemento_json][i].items() if (key in atributos_validos) }

				h.update({key:None for key in atributos_validos if key not in json_['_embedded'][elemento_json][i].keys()})
				
				resultset.append(h)


			if(offset == flush_len):
				db.bulk_insert(resultset, atributos_validos, nome_da_tabela)
				resultset = []	

		except Exception as error:
			print("Tabela:", nome_da_tabela, " - Timeout at offset: ", offset)
			print(error)

		

		offset = offset + 500



	if(len(resultset)):
		db.bulk_insert(resultset, atributos_validos, nome_da_tabela)

	print("Finalizou Dump: ", nome_da_tabela)

