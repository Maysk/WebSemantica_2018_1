import psycopg2
from config import config

def insert_uasg(ativo, cep, id_sicaf, id_municipio, id_orgao, nome, unidade_cadastradora):
	conn = None
	sql = """INSERT INTO public.uasgs(ativo, cep, id, id_municipio, id_orgao, nome, unidade_cadastradora)
	VALUES (%s, %s, %s, %s, %s, %s, %s); """
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute(sql, (ativo, cep, id_sicaf, id_municipio, id_orgao, nome, unidade_cadastradora))
		cur.commit()
		cur.close()
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

