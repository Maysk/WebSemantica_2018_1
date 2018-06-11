import psycopg2
from config import config

def insert_uasg(
		ativo = None, cep = None, ddd = None, 
		endereco = None, fax = None, id = None, 
		id_municipio = None, id_orgao = None, nome = None, 
		nome_mnemonico = None, ramal = None, ramal2 = None, 
		sigla_uf = None, telefone = None, telefone2 = None, 
		unidade_cadastradora = None):
	conn = None
	sql = """INSERT INTO public.uasgs(ativo, cep, ddd, endereco, fax, id, id_municipio, id_orgao, nome, nome_mnemonico, ramal, ramal2, sigla_uf, telefone, telefone2, unidade_cadastradora)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute(sql, (ativo, cep, ddd, endereco, fax, id, id_municipio, id_orgao, nome, nome_mnemonico, ramal, ramal2, sigla_uf, telefone, telefone2, unidade_cadastradora,))
		conn.commit()
		cur.close()
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ",error)
	finally:
		if conn is not None:
			conn.close()


def get_orgaos_relevantes():
	conn = None
	rows = []
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		sql = """SELECT DISTINCT id_orgao FROM uasgs"""
		cur.execute(sql)
		rows = cur.fetchall()
		cur.close()

	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ",error)

	finally:
		if conn is not None:
			conn.close()
		return rows
