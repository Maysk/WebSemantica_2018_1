import psycopg2
from config import config


def bulk_insert(lista_de_instancias, keys, nome_da_tabela):
	conn = None
	sql = "INSERT INTO public."+ nome_da_tabela + "(" + ",".join(keys) + ") VALUES(" + ",".join(["%("+k+")s" for k in keys]) + ");"

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for instancia in lista_de_instancias:
			cur.execute(sql, instancia)

		conn.commit()
		cur.close()
	
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	
	finally:
		if conn is not None:
			conn.close()


def get_uasgs_relevantes():
	conn = None
	rows = []
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		sql = """SELECT DISTINCT id FROM uasgs"""
		cur.execute(sql)
		rows = cur.fetchall()
		cur.close()

	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)

	finally:
		if conn is not None:
			conn.close()
		return rows
