import requests
import json 
import os


#FONTE http://compras.dados.gov.br/docs/home.html


BASE_URL = "http://compras.dados.gov.br"

def url_municipio_by_id(base_url, id_municipio):
	url_municipio = base_url + "/fornecedores/doc/municipio/" + id_municipio + ".json"
	return url_municipio

def url_fornecedor_by_id_municipio(base_url, id_municipio):
	url_fornecedor = "http://compras.dados.gov.br/fornecedores/v1/fornecedores.json?id_municipio="+ id_municipio
	return url_fornecedor


##MAIN

 

req = requests.get(url_municipio_by_id(BASE_URL, id_municipio))

if(req.status_code == 200):
	municipio_json = req.json()
	print(municipio_json['_links']['self']['title'])
	print()
	
	###Fornecedores
	url_fornecedores = url_fornecedor_by_id_municipio(BASE_URL, id_municipio)
	req = requests.get(url_fornecedores)
	if(req.status_code == 200):
		offset = 0
		fornecedores_json = req.json()
		while fornecedores_json is not None:
			fornecedores_json = req.json()
			print("Faz Alguma coisa... offset_", offset)	
			#if('next' in fornecedores_json['_links']):	
			#	fornecedores_json = BASE_URL + fornecedores_json['_links']['next']['href']
			#	offset += 500
			#else:
			#	fornecedores_json = None


	# Linha de Fornecimento

	#Codigo CNAE

	#Unidade Cadastradora

	#Orgao

	#Ocorrencia Fornecedor

	#Tipo Ocorrencia

	#Prazo Ocorrencia

	#Ambito Ocorrencia

	#Natureza Juridica

	#Ramo Negocio

	#Porte Empresa




	##################################

	#Contrato

	#Tipo Contrato

	#Contrato Aditivo

	#Contrato Apostilamento


	##################################

	#Orgao

	#Unidade Administrativa de Servico Gerais (UASG)

	#Compra

	#Item da Compra


	##################################

	#Servico

	#Secao

	#Divisao

	#Grupo

	#Classe

	#Subclasse


	##################################

	#Material

	#Grupo

	#Classe

	#Pdm


	##################################

	#Orgao

	#UASG

	#Pregao

	#Objeto

	#Tipo Pregao

	#Situacao do Pregao

	#Item do Pregao


	##################################

	#Orgao

	#UASG

	#Intencao de Registro de Preco

	#Item da intencao de registro de preco

	#participante do item da intencao de registro de preco

	#Modalidade da licitacao

	#Licitacao

	#Item da Licitacao

	#Preco praticado 

	#ITem do preco praticado

	#Registro de preco

	#Item do registro de preco

	#Fornecedor do item de registro de pre

	#Renegociacao do fornecedor do item de registro de preço